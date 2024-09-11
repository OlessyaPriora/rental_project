from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.advertisements.models import Advertisement
from apps.advertisements.permission import IsLandlordOrReadOnly
from apps.advertisements.serializers.advertisement_serializer import AdvertisementSerializer



class AdvertisementListCreateGenericView(ListCreateAPIView):
    serializer_class = AdvertisementSerializer
    queryset = Advertisement.objects.all()
    permission_classes = [IsLandlordOrReadOnly]


class AdvertisementRetrieveUpdateDestroyGenericView(RetrieveUpdateDestroyAPIView):
    serializer_class = AdvertisementSerializer
    queryset = Advertisement.objects.all()
    permission_classes = [IsAuthenticated]

   def get_object(self):





