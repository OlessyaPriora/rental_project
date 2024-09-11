from django.db import models
from apps.users.models import User


class Advertisement(models.Model):
    HOUSING_CHOICES = [
        ('apartment', 'apartment'),
        ('house', 'house'),
        ('townhouse', 'townhouse'),
    ]
    title = models.CharField(max_length=150, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    city = models.CharField(max_length=150, verbose_name="City")
    street = models.CharField(max_length=150, verbose_name="Street")
    property_number = models.PositiveSmallIntegerField(verbose_name="Property number")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    rooms = models.IntegerField(verbose_name="Rooms")
    housing_type = models.CharField(max_length=150, verbose_name="Housing Type", choices=HOUSING_CHOICES)
    is_active = models.BooleanField(default=True, verbose_name="is active")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")

    class Meta:
        verbose_name = "Advertisement"
        verbose_name_plural = "Advertisements"


    def __str__(self):
        return self.title