from data import models
import requests
from data import serializers

def get_web_url(host_path, data_path):
    host = models.Host.objects.get(path=host_path)
    web_api = models.Web_API.objects.get(host=host, path=data_path)
    return f"https://{host.domain_name}{web_api.url}"   # add api query later

def get_response_json(url):
    return requests.get(url=url).json()

def get_host_name(host_path):
    host = models.Host.objects.get(path=host_path)
    return host

def get_data_name(host_path, data_path):
    host = models.Host.objects.get(path=host_path)
    data = models.Web_API.objects.get(host=host, path=data_path)
    return data

def get_model(host_path, data_path):
    if host_path == 'my_gov':
        if data_path == 'economic-indicator':
            return {'model': models.MyGovEconomicIndicator, 'serializer': serializers.MyGovEconomicIndicatorSerializer} 
        elif data_path == 'monetory-aggregates':
            return {'model': models.MyGovMonetoryAggregates, 'serializer': serializers.MyGovMonetoryAggregatesSerializer}
        elif data_path == "household-income-by-percentile":
            return {'model': models.MyGovHouseholdIncomebyPercentile, 'serializer': serializers.MyGovHouseholdIncomebyPercentileSerializer}
        elif data_path == "household-income-and-expenditure-states":
            return {'model': models.MyGovHouseholdIncomeAndExpenditureStates, 'serializer': serializers.MyGovHouseholdIncomeAndExpenditureStatesSerializer} 
        else:
            return "Invalid data path"
    else:
        return "Invalid data path"
    
    