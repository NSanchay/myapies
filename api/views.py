from django.shortcuts import render
from rest_framework import generics,permissions
from .models import Myapi
from .serializers import Apiserializer

class Myapis(generics.ListAPIView):
    queryset= Myapi.objects.all()
    serializer_class =Apiserializer
    
class MyapiDetail(generics.RetrieveAPIView):
    permission_classes=(permissions.IsAuthenticated,)
    queryset= Myapi.objects.all()
    serializer_class = Apiserializer

class MyapiCreate(generics.ListCreateAPIView):
    permission_classes=(permissions.IsAuthenticated,)
    queryset = Myapi.objects.all()
    serializer_class = Apiserializer
    
class MyapiUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(permissions.IsAuthenticated,)
    queryset = Myapi.objects.all()
    serializer_class = Apiserializer
# Create your views here.
