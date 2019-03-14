from django.urls import path
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ListCreateCar

app_name = 'cars'

urlpatterns = {
    url(r'^cars/$', ListCreateCar.as_view(), name="create")
}

urlpatterns = format_suffix_patterns(urlpatterns)