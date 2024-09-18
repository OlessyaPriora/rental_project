from django.urls import path
from apps.advertisements.views.advertisement_views import *

urlpatterns = [
    #Путь для просмотра и создания объявлений
    path('', AdvertisementListCreateGenericView.as_view(), name='advertisement-list-create'),
    #Путь для обновления и удаления объявления, только landlord
    path('<int:pk>/', AdvertisementRetrieveUpdateDestroyGenericView.as_view(), name='advertisement-update-destroy'),
]