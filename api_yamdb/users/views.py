from django.shortcuts import get_object_or_404
from rest_framework import mixins, permissions, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import UsersByAdminSerializer, UserSerializer


class UserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """Самостоятельная регистрация новых пользователей."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)


@api_view(["POST"])
@permission_classes([AllowAny])
def token(request):
    """Токен."""
    user = get_object_or_404(User, username=request.data.get("username"))
    confirmation_code = request.data.get("confirmation_code")
    if not confirmation_code:
        return Response(["confirmation_code is required."], status=400)
    if str(confirmation_code) != str(user.confirmation_code):
        return Response(
            ["Incorrect confirmation_code"],
            status=401,
        )
    refresh = RefreshToken.for_user(user)
    return Response(
        {
            "token": str(refresh.access_token),
        }
    )


class UsersByAdminViewSet(viewsets.ModelViewSet):
    """Управление пользователями администратором."""

    queryset = User.objects.all()
    serializer_class = UsersByAdminSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAdminUser,)

    # https://stackoverflow.com/questions/30170848/how-can-i-make-a-django-rest-framework-me-call
    @action(
        methods=("GET", "PATCH"), detail=False, url_path="me", url_name="me"
    )
    def me(self, request, *args, **kwargs):
        """ПОКА НЕ РАБОТАЕТ МЕТОД PATCH."""
        self.kwargs.update(pk=request.user.id)
        return self.retrieve(request, *args, **kwargs)
