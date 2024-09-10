from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from apps.users.serializers.user_serializer import UserListSerializer


class UserListGenericView(ListAPIView):
    serializer_class = UserListSerializer