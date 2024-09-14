from django.urls import path, include


urlpatterns = [
    path('users/', include('apps.users.urls')),
    path('ads/', include('apps.advertisements.urls')),
    path('bookings/', include('apps.bookings.urls')),
]
