from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PlaceSerializer, TourSerializer
from .models import Place, Tour
# Create your views here.

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all().order_by('ordering')
    serializer_class = PlaceSerializer
    
    
class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer