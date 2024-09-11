from django.urls import path
from apps.advertisements.views.advertisement_views import *

urlpatterns = [
    path('', AdvertisementListCreateGenericView.as_view(), name='advertisement-list-create'),
]