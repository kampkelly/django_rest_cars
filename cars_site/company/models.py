from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=250,unique=True,null=False)
    location = models.CharField(max_length=250,null=False)
    image = models.CharField(max_length=250,null=True)
    established_year = models.DateField(null=False)
    rating = models.CharField(max_length=250,null=True)

    def __str__(self):
        """A string representation of the model."""
        return self.name