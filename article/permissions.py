from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # 对所有人允许get head option
        if request.method in permissions.SAFE_METHODS:
            return True
        # 管理员允许其他操作
        return request.user.is_superuser
