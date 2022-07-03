from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Myapi

class Apiserializer(serializers.ModelSerializer):
    class Meta:
        model= Myapi
        fields = ('id','title', 'img','img2','desc','price', 'rating')