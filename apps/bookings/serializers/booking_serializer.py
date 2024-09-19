from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from apps.advertisements.serializers.advertisement_serializer import AdvertisementSerializer
from apps.bookings.models import Booking
from django.utils import timezone
from rest_framework.exceptions import ValidationError
import datetime


class BookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'advertisement', 'start_date', 'end_date', 'total_cost']
        read_only_fields = ['id', 'total_cost']

    def validate_advertisement(self, advertisement):
        if not advertisement.is_active:
            raise serializers.ValidationError('Advertisement is not active')
        return advertisement

    def validate(self, data):
        today = datetime.date.today()
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        advertisement = data.get('advertisement')

        # Проверка даты начала
        if start_date < today:
            raise ValidationError({'start_date': 'Booking start date cannot be earlier than today'})

        # Проверка даты окончания
        if start_date > end_date:
            raise ValidationError({'start_date': 'The booking start date cannot be after the booking end date'})

        # Проверка на пересечение бронирований для конкретного объявления
        if advertisement:
            conflicting_bookings = Booking.objects.filter(
                advertisement=advertisement,
                status__in=['pending', 'confirmed'],# Только для конкретного объявления
                start_date__lt=end_date,      # Если начальная дата бронирования меньше даты окончания нового бронирования
                end_date__gt=start_date       # И дата окончания бронирования больше начальной даты нового бронирования
            ).exclude(pk=self.instance.pk if self.instance else None)

            if conflicting_bookings.exists():
                raise ValidationError({'start_date': 'The booking dates overlap with an existing booking for this advertisement'})

        return data

    def create(self, validated_data):
        user = self.context['request'].user
        author = validated_data['advertisement'].author

        validated_data['tenant'] = user
        validated_data['landlord'] = author

        return super().create(validated_data)


class BookingListSerializer(serializers.ModelSerializer):
    advertisement = AdvertisementSerializer(read_only=True)
    tenant = StringRelatedField()
    landlord = StringRelatedField()
    class Meta:
        model = Booking
        fields = ['id', 'advertisement', 'start_date', 'end_date', 'total_cost', 'status', 'tenant', 'landlord']



class BookingRetrieveUpdateTenantSerializer(serializers.ModelSerializer):
    advertisement = AdvertisementSerializer(read_only=True)
    tenant = StringRelatedField(read_only=True)
    landlord = StringRelatedField(read_only=True)
    class Meta:
        model = Booking
        exclude = ['created_at', 'updated_at']
        read_only_fields = ['start_date', 'end_date']

    def validate(self, data):
        status = data.get('status')
        start_date = self.instance.start_date


        if status == "rejected":
            if start_date < timezone.now().date() + timezone.timedelta(days=2):
                raise serializers.ValidationError(
                    {'status': 'Booking cannot be rejected if start date is within the next 2 days.'})
        elif status in ["confirmed", "pending"]:
            raise serializers.ValidationError(
                {'status': 'Tenant can not change the status to "confirmed" or "pending"'})

        return data

class BookingRetrieveUpdateLandlordSerializer(serializers.ModelSerializer):
    advertisement = AdvertisementSerializer(read_only=True)
    tenant = StringRelatedField(read_only=True)
    landlord = StringRelatedField(read_only=True)
    class Meta:
        model = Booking
        exclude = ['created_at', 'updated_at']
        read_only_fields = ['start_date', 'end_date']

    def validate(self, data):
        status = data.get('status')
        start_date = self.instance.start_date

        if status == "rejected":
            if start_date < datetime.date.today() + datetime.timedelta(days=2):
                raise serializers.ValidationError(
                    {'status': 'Booking cannot be rejected if start date is within the next 2 days.'})
        elif status == "pending":
            raise serializers.ValidationError(
                {'status': 'Landlord can not change the status to "pending"'})

        return data

#Сериализатор чтоб пользователь мог видеть забронированные даты определённого объявления
class BookingDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['start_date', 'end_date']
