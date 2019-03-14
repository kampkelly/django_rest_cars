from django.shortcuts import render
from rest_framework import generics

from .serializers import CarSerializer
from cars.models import Car

class ListCreateCar(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Car.objects.all()
    serializer_class = CarSerializer
