from rest_framework.permissions import BasePermission

class IsEmployer(BasePermission):
    def has_permission(self, request, view):
        result = request.user.role=="employer"
        result = result or request.user.is_superuser==True
        return result
    


