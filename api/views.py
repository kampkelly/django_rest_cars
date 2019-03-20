from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters

from .serializers import CarSerializer
from cars_site.cars.models import Car

class CarFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='iexact')
    color = filters.CharFilter(lookup_expr='iexact')
    kind = filters.CharFilter(lookup_expr='iexact')
    milleage = filters.NumberFilter(lookup_expr='lt')

    class Meta:
        model = Car
        fields = []


class ListCar(generics.ListAPIView):
    """This class defines the list behavior of our rest api."""
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filterset_class = CarFilter


class CreateCar(generics.CreateAPIView):
    """This class defines the create behavior of our rest api."""
    permission_classes = (IsAuthenticated,) 
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class RetrieveUpdateDestroyCar(generics.RetrieveUpdateDestroyAPIView):
    """This class defines the http retrieve, update and delete requests of our rest api."""
    permission_classes = (IsAuthenticated,) 
    queryset = Car.objects.all()
    serializer_class = CarSerializer
