from django.urls import path
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateCar, RetrieveUpdateDestroyCar, ListCar

app_name = 'cars'

urlpatterns = {
    url(r'^cars/create/$', CreateCar.as_view(), name="create"),
    url(r'^cars/(?P<pk>[0-9]+)/$', RetrieveUpdateDestroyCar.as_view(), name="details"),
    url(r'^cars\.??(?:&?[^=&]*=[^=&]*)*', ListCar.as_view(), name="list")
}

urlpatterns = format_suffix_patterns(urlpatterns)
