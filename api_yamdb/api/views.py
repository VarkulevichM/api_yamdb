from api.serializers import (CategorySerializer, CommentSerializer,
                             GenreSerializer, ReviewSerializer,
                             TitleSerializer, TitleSerializerGET)
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import (AllowAny, IsAdminUser, IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from reviews.models import Category, Comment, Genre, Review, Title

from .permissions import (IsAdmin, IsAdminModeratorAuthorOrReadOnly,
                          IsAdminOrReadOnly)


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (
        IsAdminModeratorAuthorOrReadOnly,
        IsAuthenticatedOrReadOnly
        )
    pagination_class = PageNumberPagination

    def get_queryset(self):
        title = get_object_or_404(Title, id=self.kwargs['title_id'])
        return title.reviews.all()
    
    def perform_create(self, serializer):
        title = get_object_or_404(Title, id=self.kwargs['title_id'])
        serializer.save(author=self.request.user, title=title)

    def perform_update(self, serializer):
        review = get_object_or_404(Review,id=self.kwargs['review_id'])
        serializer.save(author=self.request.user, review=review)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (
        IsAdminModeratorAuthorOrReadOnly,
        IsAuthenticatedOrReadOnly
        )
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter,)
    search_fields = ('title_id',)

    def get_queryset(self):
        review = get_object_or_404(
            Review,
            title_id=self.kwargs.get('title_id'),
            id=self.kwargs.get('review_id'),
        )
        return review.comments.all()

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, id=review_id, title=title_id)
        serializer.save(
            author=self.request.user,
            review=review
        )


class CategoryViewSet(viewsets.ModelViewSet):
    """Вьюсет создания обьектов модели Category"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    search_fields = ("name",)


class GenreViewSet(viewsets.ModelViewSet):
    """Вьюсет создания обьектов модели Genre"""
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    search_fields = ("name",)


class TitleViewSet(viewsets.ModelViewSet):
    """Вьюсет создания обьектов модели Title"""
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("category", "genre", "name", "year")

    def get_serializer_class(self):
        """Метод, в котором выбирается какой из сериализаторов
        будет использоваться в зависимости от метода запроса
        """
        if self.request == "GET":
            return TitleSerializerGET
        return TitleSerializer
