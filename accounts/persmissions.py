from rest_framework.permissions import BasePermission

class IsAdminOrIsUserSelf(BasePermission):
    
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        else:
            return bool(obj.pk == request.user.pk)