from rest_framework import permissions


class IsAdministrator(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.role == "AD":
            return True


class IsWaiter(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.role == "WT":
            return True


class IsCook(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.role == "CK":
            return True
