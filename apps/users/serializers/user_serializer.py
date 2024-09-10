from rest_framework import serializers
from apps.users.models import User
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class RegisterUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'password', 'name')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        name = data.get('name')

        if not re.match('^[a-zA-Z0-9_]*$', name):
            raise serializers.ValidationError(
                "The name must be alphanumeric characters or have only _ symbol"
            )

        password = data.get('password')

        try:
            validate_password(password)
        except ValidationError as err:
            raise serializers.ValidationError({"password": err.messages})

        return data

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user