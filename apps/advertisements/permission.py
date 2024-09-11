from rest_framework.permissions import BasePermission


class IsLandlordOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return request.user.role == 'Landlord'