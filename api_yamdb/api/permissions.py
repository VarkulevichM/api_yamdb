from rest_framework import permissions


class AdminOrReadOnly(permissions.BasePermission):
    """Разрешения для TitleViewSet, GenreViewSet, CategoryViewSet"""

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS or (
            request.user.is_authenticated
            and (request.user.role == "admin" or request.user.is_superuser)
        )


class AdminModeratorAuthorOrReadOnly(permissions.BasePermission):
    """Разрешения для CommentViewSet,ReviewViewSet"""

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.role == "admin"
            or request.user.role == "moderator"
            or obj.author == request.user
        )

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )
