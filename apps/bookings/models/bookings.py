from datetime import timedelta
from django.db import models
from rest_framework.exceptions import ValidationError
from apps.advertisements.models import Advertisement
from apps.users.models import User
from apps.bookings.models import *


class Booking(models.Model):
    BOOKING_CHOICES = [
        ('pending', 'pending'),
        ('confirmed', 'confirmed'),
        ('rejected', 'rejected'),
    ]
    tenant = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name= 'tenant', related_name='tenant_bookings')
    landlord = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name= 'landlord', related_name='landlord_bookings')
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    start_date = models.DateField(verbose_name = 'start date', unique=True)
    end_date = models.DateField(verbose_name = 'end date', unique=True)
    status = models.CharField(max_length=10, default='pending', choices=BOOKING_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = 'booking'
        verbose_name_plural = 'bookings'
        ordering = ['created_at']

    def __str__(self):
        return f'Booking {self.pk} for {self.advertisement} from {self.start_date} to {self.end_date} by {self.tenant.name} and landlord {self.landlord.name}'


@property
def total_cost(self):
    return self.advertisement.price * (self.end_date - self.start_date)

@property
def booking_dates(self):
    bookings = Booking.objects.filter(advertisement=self.advertisement).exclude(pk=self.pk)
    return [date for booking in bookings for date in range(booking.start_date, booking.end_date + timedelta(days=1))]