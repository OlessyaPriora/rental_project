from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from apps.bookings.permissions import IsTenant
from apps.reviews.models import Review
from apps.reviews.serializers.review_serializer import *


class ReviewCreateGenericView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewCreateSerializer
    permission_classes = (IsTenant)  # Проверяем, что пользователь арендовал жилье

class ReviewListGenericView(ListAPIView):
    serializer_class = ReviewListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        advertisement_id = self.kwargs['advertisement_id']
        return Review.objects.filter(advertisement__id=advertisement_id)