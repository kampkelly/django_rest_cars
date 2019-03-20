from rest_framework import serializers
from cars_site.cars import models


class CarSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = models.Car
        fields = ('id', 'name', 'kind', 'year_of_creation', 'milleage', 'color', 'car_maker', 'is_available', 'car_engine_no', 'deleted', 'status', 'price')
        read_only_fields = ('',)
