from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters

from .serializers import CompanySerializer
from .models import Company

class ListCreateCompany(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    permission_classes = (IsAuthenticated,) 
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class RetrieveUpdateDestroyCompany(generics.RetrieveUpdateDestroyAPIView):
    """This class defines the http retrieve, update and delete requests of our rest api."""
    permission_classes = (IsAuthenticated,) 
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
