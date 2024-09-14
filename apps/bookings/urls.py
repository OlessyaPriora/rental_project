from django.urls import path
from apps.bookings.views.booking_views import *

urlpatterns = [
    #создание бронирования для арендатора(tenant)
    path('tenant/', BookingActiveListCreateGenericView.as_view(), name='booking-active-list-create-tenant'),
    # Просмотр прошлых бронирований для арендатора(tenant)
    path('tenant/past/', BookingPastListTenantGenericView.as_view(), name='booking-past-list-tenant'),
    # Просмотр активных бронирований своих объявлений для арендодателя(landlord)
    path('landlord/active/', BookingActiveListGenericView.as_view(), name='booking-active-list-landlord'),
    # Просмотр прошлых бронирований своих объявлений для арендодателя(landlord)
    path('landlord/past/', BookingPastListGenericView.as_view(), name='booking-past-list-landlord'),
    #Обновление статуса отклонения бронирования для арендатора(tenant)
    path('tenant/<int:pk>/', BookingRetrieveUpdateTenantGenericView.as_view(), name='booking-update-tenant'),
    #Обновление статуса бронирования для арендодателя (подтвердить или отклонить)
    path('landlord/<int:pk>/', BookingRetrieveUpdateLandlordGenericView.as_view(), name='booking-update-landlord'),
    #Просмотр по id объявления уже забронированные даты, могут видеть landlord & tenant
    path('ads/<int:advertisement_id>/', BookingAdvertisementDatesListView.as_view(), name='booked-dates'),
]