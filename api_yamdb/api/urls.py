from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from api.views import CategoryViewSet
from api.views import GenreViewSet
from api.views import TitleViewSet

v1_router = DefaultRouter()
v1_router.register(
    "categories",
    CategoryViewSet,
    basename="category"
)
v1_router.register(
    "genres",
    GenreViewSet,
    basename="genre"
)
v1_router.register(
    "titles",
    TitleViewSet,
    basename="title"
)

urlpatterns = [
    path("v1/", include(v1_router.urls))
]
