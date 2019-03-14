from django.shortcuts import render
from rest_framework import generics

from .serializers import CarSerializer
from cars.models import Car

class ListCreateCar(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class RetrieveUpdateDestroyCar(generics.RetrieveUpdateDestroyAPIView):
    """This class defines the http retrieve, update and delete requests of our rest api."""
    queryset = Car.objects.all()
    serializer_class = CarSerializer
