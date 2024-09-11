from rest_framework import serializers, status
from rest_framework.response import Response
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
        fields = ('email', 'password', 'name', 'role')
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

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance, validated_data)




