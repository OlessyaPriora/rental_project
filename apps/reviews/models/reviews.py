from django.db import models
from apps.advertisements.models import Advertisement
from apps.users.models import User


class Review(models.Model):
    tenant = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='tenant', related_name='reviews')
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False) # Поле не может быть изменено пользователем
    comment = models.TextField(null=True, blank=True) # Позволяет полю быть пустым, т.е. пользователь может не зап-ть его
    rating = models.IntegerField()


    class Meta:
        verbose_name = 'review'
        verbose_name_plural = 'reviews'
        unique_together = ['tenant', 'advertisement']

    def __str__(self):
        return self.rating