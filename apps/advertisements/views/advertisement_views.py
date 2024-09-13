from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from apps.advertisements.models import Advertisement
from apps.advertisements.permission import IsLandlordOrReadOnly, IsAuthorOrReadOnly
from apps.advertisements.serializers.advertisement_serializer import AdvertisementSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend



class AdvertisementListCreateGenericView(ListCreateAPIView):
    serializer_class = AdvertisementSerializer
    queryset = Advertisement.objects.all()
    permission_classes = [IsLandlordOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
        'price': ['gte', 'lte'],
        'city': ['icontains'],
        'rooms': ['gte', 'lte'],
        'housing_type': ['exact'],
}
    search_fields = ['title', 'description']
    ordering_fields = ['price', 'created_at']


    def get_queryset(self):
        return Advertisement.objects.filter(is_active=True)


class AdvertisementRetrieveUpdateDestroyGenericView(RetrieveUpdateDestroyAPIView):
    serializer_class = AdvertisementSerializer
    queryset = Advertisement.objects.all()
    permission_classes = [IsAuthorOrReadOnly]












