from os import path
from django.shortcuts import render
from data.src import common, updater
from django.core.serializers import serialize
from django.http import JsonResponse
from django.http import HttpResponse
import requests
from rest_framework.parsers import JSONParser
from .models import Web_API, Host
from .serializers import Web_APISerializer, HostSerializer
from django.views.decorators.csrf import csrf_exempt

# GENERIC CODES

def index(request):
    return HttpResponse("Welcome to Malaysia Macroeconomic Analysis Page")

def host_index(request,host_path):
    hostname = common.get_host_name(host_path=host_path)
    return HttpResponse(f"{hostname}")

def data_index(request, host_path, data_path):
    dataname = common.get_data_name(host_path, data_path)
    return HttpResponse(f"{dataname}")

def updates(request, host_path, data_path):
    url = common.get_web_url(host_path, data_path) + "&limit=3"
    try:
        response_json = common.get_response_json(url)
        if response_json:  # Check if response is not empty
            column_names = response_json[0].keys()
        else:
            column_names = []  # Empty list if response is empty
        context = {
            "data_list": response_json,
            "column_names": column_names,
        }
        return render(request, "data/table_response_json.html", context)
    except Exception as e:
        return HttpResponse("An error occurred: " + str(e))
    
def table(request, host_path, data_path):
    try:
        model = common.get_model(host_path, data_path)['model']
        data_list = model.objects.all()
        column_names = [field.name for field in model._meta.get_fields() if field.name != 'id']

        # Create a dictionary to store values of specific columns
        rows = []
        for item in data_list:
            row = {}
            for column in column_names:
                row[column] = getattr(item, column)
            rows.append(row)
            
        context = {
            "data_list": rows,
            "column_names": column_names,
        }
            
        print(rows)
        return render(request, 'data/table_response_json.html', context)
    except Exception as e:
        return HttpResponse("An error occurred: " + str(e))


# update database
def update_db(request, host_path, data_path):
    url = common.get_web_url(host_path, data_path)
    response_json = requests.get(url=url).json()
    return HttpResponse(updater.updateDB(host_path, data_path, response_json))


# GET/POST JSON DATA 
@csrf_exempt
def web_api_list(request, host_path, *args, **kwargs):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        host = Host.objects.get(path=host_path)
        data = Web_API.objects.filter(host=host)
        serializer = Web_APISerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Web_APISerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    
@csrf_exempt
def host_list(request, *args, **kwargs):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        data = Host.objects.all()
        serializer = HostSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = HostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def data_list(request, host_path, data_path, *args, **kwargs):
    temp = common.get_model(host_path, data_path)
    model = temp['model']
    model_serializer = temp['serializer']
    if request.method == 'GET':
        data = model.objects.all()
        serializer = model_serializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = model_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)