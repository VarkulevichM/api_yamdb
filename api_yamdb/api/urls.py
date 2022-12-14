from django.urls import include
from django.urls import path
from rest_framework.routers import SimpleRouter

from api.views import CommentViewSet
from api.views import ReviewViewSet
from api.views import CategoryViewSet
from api.views import GenreViewSet
from api.views import TitleViewSet


app_name = 'api'

router = SimpleRouter()
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router.register(
    "categories",
    CategoryViewSet,
    basename="category"
)
router.register(
    "genres",
    GenreViewSet,
    basename="genre"
)
router.register(
    "titles",
    TitleViewSet,
    basename="title"
)

urlpatterns = [
    path('v1/', include(router.urls)),
]
