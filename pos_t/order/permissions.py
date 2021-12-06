from rest_framework import permissions


class IsAdministrator(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.role == "AD" and request.user.is_active:
            return True


class IsWaiter(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.role == "WT" and request.user.is_active:
            return True


class IsCook(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.role == "CK" and request.user.is_active:
            return True
