from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from apps.advertisements.models import Advertisement
from apps.advertisements.permission import IsLandlordOrReadOnly, IsAuthorOrReadOnly
from apps.advertisements.serializers.advertisement_serializer import AdvertisementSerializer



class AdvertisementListCreateGenericView(ListCreateAPIView):
    serializer_class = AdvertisementSerializer
    queryset = Advertisement.objects.all()
    permission_classes = [IsLandlordOrReadOnly]

    def get_queryset(self):
        return Advertisement.objects.filter(is_active=True)


class AdvertisementRetrieveUpdateDestroyGenericView(RetrieveUpdateDestroyAPIView):
    serializer_class = AdvertisementSerializer
    queryset = Advertisement.objects.all()
    permission_classes = [IsAuthorOrReadOnly]







