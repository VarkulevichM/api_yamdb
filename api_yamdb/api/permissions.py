from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    message = 'Проверьте, что запрос осуществляет админ или суперюзер'

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin


class IsAdminOrReadOnly(permissions.BasePermission):
    message = 'Проверьте, что запрос осуществляет админ или суперюзер \
        или будет доступ только для чтения'

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or (request.user.is_authenticated and request.user.is_admin))


class IsAdminModeratorAuthorOrReadOnly(permissions.BasePermission):
    message = ('Только для чтения, если не админ, модератор или автор')

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user
                or request.user.is_moderator
                or request.user.is_admin)
