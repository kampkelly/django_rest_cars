from rest_framework import serializers
from cars_site.cars.models import Car
from cars_site.company.models import Company

class CompanySerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Company
        fields = ('id', 'name', 'location', 'image', 'established_year', 'rating')
        read_only_fields = ('',)


class CarSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    company_id = serializers.IntegerField()

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Car
        fields = ('id', 'name', 'kind', 'year_of_creation', 'milleage', 'color', 'car_maker', 'is_available', 'car_engine_no', 'deleted', 'status', 'price', 'company_id')
        read_only_fields = ('',)

    def create(self, validated_data):
        company_id = validated_data.get('company_id')
        selected_company = Company.objects.get(id=company_id)
        car = Car(company=selected_company, **validated_data)
        car.save()
        return car
