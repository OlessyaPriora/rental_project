from datetime import datetime
from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from apps.bookings.models import Booking
from apps.reviews.models import Review

#для создания отзывов и рейтингов
class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('advertisement', 'comment', 'rating')

    def validate(self, data):
        tenant = self.context['request'].user
        advertisement = data['advertisement']
        booking = Booking.objects.filter(
            advertisement=advertisement,
            tenant=tenant,
            status='confirmed',
            end_date__lte=datetime.date.today()).exists()

        if not booking:
            raise serializers.ValidationError('You do not have permission to perform this action, because you have not booked this property')

        review = Review.objects.filter(
            tenant=tenant,
            advertisement=advertisement).exists()
        if review:
            raise serializers.ValidationError('You have already review about this property')
        return data

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError('Rating must be between 1 and 5')
        return value

    def create(self, validated_data):
        validated_data['tenant'] = self.context['request'].user
        return super().create(validated_data)

class ReviewListSerializer(serializers.ModelSerializer):
    tenant = StringRelatedField()
    advertisement = StringRelatedField()

    class Meta:
        model = Review
        fields = '__all__'






