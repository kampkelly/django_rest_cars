from django.shortcuts import render
from rest_framework import generics

from .serializers import CarSerializer
from cars.models import Car


class ListCar(generics.ListAPIView):
    """This class defines the list behavior of our rest api."""
    serializer_class = CarSerializer

    def get_queryset(self):
        """
        This view should return a list of all the cars (filtered
        by query parameters passed)
        """
        queryset = Car.objects.all()
        car_name = self.request.query_params.get('name', None)
        params = [(param, self.request.query_params.get(param, None)) for param in self.request.query_params if self.request.query_params.get(param) != None]
        if params:
            queryset = queryset.filter(name=car_name)
        return queryset


class CreateCar(generics.CreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class RetrieveUpdateDestroyCar(generics.RetrieveUpdateDestroyAPIView):
    """This class defines the http retrieve, update and delete requests of our rest api."""
    queryset = Car.objects.all()
    serializer_class = CarSerializer
