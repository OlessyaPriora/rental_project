import re
from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from apps.advertisements.models import Advertisement

class AdvertisementSerializer(serializers.ModelSerializer):
    author = StringRelatedField(read_only=True)
    class Meta:
        model = Advertisement
        fields = '__all__'

# Валидация на проверку названия объявления
    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError('The minimum length must be greater than or equal to 5 letters')
        if len(value) > 150:
            raise serializers.ValidationError('The maximum length must be less than 150 letters')
        return value

# Валидация на проверку описания объявления
    def validate_description(self, value):
        if len(value) < 10:
            raise serializers.ValidationError('The minimum length must be greater than or equal to 10 letters')
        if len(value) > 500:
            raise serializers.ValidationError('The maximum length must be less than 500 letters')
        return value

# Валидация на проверку названия города
    def validate_city(self, value):
        if not re.match(r'^([a-zA-Z ]{2,50})$', value):
            raise serializers.ValidationError('The city must be represented by alphabetic characters')
        return value

# Валидация на проверку названия улицы
    def validate_street(self, value):
        if len(value) < 4:
            raise serializers.ValidationError('The minimum length must be greater than or equal to 4 letters')
        if len(value) > 150:
            raise serializers.ValidationError('The maximum length must be less than 150 letters')
        return value

# Валидация на проверку номера дома
    def validate_property_number(self, value):
        if value < 1:
            raise serializers.ValidationError('Property number must be greater than or equal to 1')
        return value

# Валидация на проверку цены
    def validate_price(self, value):
        if value < 1:
            raise serializers.ValidationError('The price must be greater than or equal to 1')
        return value

# Валидация на проверку количества комнат
    def validate_rooms(self, value):
        if value < 1:
            raise serializers.ValidationError('Room must be greater than or equal to 1')
        return value
