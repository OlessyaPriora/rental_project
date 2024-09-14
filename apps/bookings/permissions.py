from rest_framework import permissions


class IsTenant(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == "Tenant"

class IsLandlord(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == "Landlord"
