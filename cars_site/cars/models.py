from django.db import models
from cars_site.company.models import Company

class Car(models.Model):
    name = models.CharField(max_length=250,unique=True,null=False)
    kind = models.CharField(max_length=250,null=False)
    year_of_creation = models.DateTimeField(null=False)
    milleage = models.IntegerField(null=True,default=0)
    color = models.CharField(max_length=250,null=True)
    is_available = models.BooleanField(null=False,default=False)
    car_engine_no = models.CharField(max_length=250,null=True,unique=True)
    deleted = models.BooleanField(null=True,default=False)
    status = models.CharField(max_length=250,null=False,default='new')
    price = models.FloatField(null=False,default=0.00)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        """A string representation of the model."""
        return self.name