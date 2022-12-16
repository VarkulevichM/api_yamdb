from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination

from api.filters import TitlesFilter
from api.permissions import AdminOrReadOnly
from api.serializers import CategorySerializer
from api.serializers import CommentSerializer
from api.serializers import GenreSerializer
from api.serializers import ReviewSerializer
from api.serializers import TitleSerializer
from api.serializers import TitleSerializerGET
from reviews.models import Category
from reviews.models import Genre
from reviews.models import Review
from reviews.models import Title


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [] # пока ничего, надо согласовать пермишны
    pagination_class = PageNumberPagination

    def get_queryset(self):
        title = get_object_or_404(
            Title,
            id=self.kwargs.get('title_id')
        )
        return title.rewiews.all()
    
    def perform_create(self, serializer):
        title = get_object_or_404(
            Title,
            id=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [] # пока ничего, надо согласовать пермишны
    pagination_class = PageNumberPagination

    def get_queryset(self):
        rewiew = get_object_or_404(
            Review,
            id=self.kwargs.get('rewiew_id')
        )
        return rewiew.comments.all()

    def perform_create(self, serializer):
        rewiew = get_object_or_404(
            Review,
            id=self.kwargs.get('rewiew_id')
        )
        serializer.save(author=self.request.user, rewiew=rewiew)


class CategoryViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    """Вьюсет создания обьектов модели Category"""

    queryset = Category.objects.all().order_by("id")
    serializer_class = CategorySerializer
    permission_classes = (AdminOrReadOnly,)
    filter_backends = (SearchFilter,)
    search_fields = ("name",)
    lookup_field = "slug"


class GenreViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    """Вьюсет создания обьектов модели Genre"""

    queryset = Genre.objects.all().order_by("id")
    serializer_class = GenreSerializer
    permission_classes = (AdminOrReadOnly,)
    filter_backends = (SearchFilter,)
    search_fields = ("name",)
    lookup_field = "slug"


class TitleViewSet(viewsets.ModelViewSet):
    """Вьюсет создания обьектов модели Title"""

    queryset = Title.objects.all().order_by("id")
    permission_classes = (AdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitlesFilter

    def get_serializer_class(self):
        """Метод, в котором выбирается какой из сериализаторов
        будет использоваться в зависимости от метода запроса.
        """

        if self.action in ("list", "retrieve"):
            return TitleSerializerGET
        return TitleSerializer
