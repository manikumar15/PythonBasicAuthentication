from django.shortcuts import render

from .models import Data
from .serializers import Dataserializer

from rest_framework import viewsets

class DataViewSet(viewsets.ModelViewSet):
	queryset=Data.objects.all()
	serializer_class=Dataserializer