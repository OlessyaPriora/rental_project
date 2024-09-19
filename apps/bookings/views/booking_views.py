from datetime import date
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from apps.bookings.permissions import IsTenant, IsLandlord
from apps.bookings.serializers.booking_serializer import *


class BookingActiveListCreateGenericView(ListCreateAPIView): # список активных бронирований для арендатора и создание новых бронировний
    queryset = Booking.objects.all()
    permission_classes = [IsTenant]

    def get_queryset(self):
        return Booking.objects.filter(tenant=self.request.user, start_date__gte=date.today())

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BookingCreateSerializer
        return BookingListSerializer

class BookingPastListTenantGenericView(ListAPIView): # список завершеных бронирований для арендатора
    queryset = Booking.objects.all()
    serializer_class = BookingListSerializer
    permission_classes = [IsTenant]

    def get_queryset(self):
        return Booking.objects.filter(tenant=self.request.user, start_date__lt=date.today())

class BookingActiveListGenericView(ListAPIView): # список активных бронирований для арендодателя
    queryset = Booking.objects.all()
    serializer_class = BookingListSerializer
    permission_classes = [IsLandlord]

    def get_queryset(self):
        return Booking.objects.filter(landlord=self.request.user, start_date__gte=date.today())

class BookingPastListGenericView(ListAPIView): # список завершеных бронирований для арендодателя
    queryset = Booking.objects.all()
    serializer_class = BookingListSerializer
    permission_classes = [IsLandlord]

    def get_queryset(self):
        return Booking.objects.filter(landlord=self.request.user, start_date__lt=date.today())


class BookingRetrieveUpdateTenantGenericView(RetrieveUpdateAPIView): # изменение статус бронирования для арендатора
    queryset = Booking.objects.all()
    serializer_class = BookingRetrieveUpdateTenantSerializer
    permission_classes = [IsTenant]

    def get_queryset(self):
        return Booking.objects.filter(tenant=self.request.user)


class BookingRetrieveUpdateLandlordGenericView(RetrieveUpdateAPIView):  # изменение статус бронирования для арендатодателя
    queryset = Booking.objects.all()
    serializer_class = BookingRetrieveUpdateLandlordSerializer
    permission_classes = [IsLandlord]

    def get_queryset(self):
        return Booking.objects.filter(landlord=self.request.user)


class BookingAdvertisementDatesListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BookingDateSerializer

    def get_queryset(self):
        advertisement_id = self.kwargs['advertisement_id']  # Получаем ID объявления из URL
        return Booking.objects.filter(
            advertisement_id=advertisement_id,
            status__in=['pending', 'confirmed'],
            end_date__gte=date.today()  # Забронированные даты, которые не закончились
        ).values('start_date', 'end_date')  # Возвращаем только даты





