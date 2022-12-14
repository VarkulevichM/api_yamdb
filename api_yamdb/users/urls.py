from django.urls import path, include
from .views import UserViewSet, token, UsersByAdminViewSet
from rest_framework import routers

user_create = UserViewSet.as_view({"post": "create"})

router = routers.SimpleRouter()
router.register(r"users", UsersByAdminViewSet)

urlpatterns = [
    path("signup/", user_create, name="user-create"),
    path("token/", token, name="token"),
    path("", include(router.urls)),
]
