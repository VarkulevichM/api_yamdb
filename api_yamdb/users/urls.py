from django.urls import include, path
from rest_framework import routers

from .views import UsersByAdminViewSet, UserViewSet, token

user_create = UserViewSet.as_view({"post": "create"})

router = routers.SimpleRouter()
router.register(r"users", UsersByAdminViewSet)

urlpatterns = [
    path("signup/", user_create, name="user-create"),
    path("token/", token, name="token"),
    path("", include(router.urls)),
]
