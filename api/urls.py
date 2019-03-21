from django.urls import path
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt import views as jwt_views

from .views import CreateCar, RetrieveUpdateDestroyCar, ListCar, ListCreateCompany, RetrieveUpdateDestroyCompany

app_name = 'cars'

urlpatterns = {
    url(r'^cars/$', CreateCar.as_view(), name="create"),
    url(r'^cars/(\w\D)??(?:&?[^=&]*=[^=&]*)*', ListCar.as_view(), name="list"),
    url(r'^cars/(?P<pk>[0-9]+)$', RetrieveUpdateDestroyCar.as_view(), name="details"),
    url('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    url(r'^company/$', ListCreateCompany.as_view(), name="create_company"),
    url(r'^company/(?P<pk>[0-9]+)$', RetrieveUpdateDestroyCompany.as_view(), name="details_of_company"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
