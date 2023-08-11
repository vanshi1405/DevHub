from rest_framework.permissions import BasePermission


class CustomGroupPermissions(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if view.action in ["list", "retrieve", "create", "update"] and user.is_superuser:
            return True
        if view.action in ["list", "retrieve",] and not user.is_superuser:
            return True
        return False