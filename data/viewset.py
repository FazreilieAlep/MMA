from rest_framework import viewsets
from .models import Web_API
from .serializers import Web_APISerializer

class WebAPIViewSet(viewsets.ModelViewSet):
    queryset = Web_API.objects.all()
    serializer_class = Web_APISerializer
