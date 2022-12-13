from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from api.serializers import CategorySerializer
from api.serializers import GenreSerializer
from api.serializers import TitleSerializer
from api.serializers import TitleSerializerGET
from reviews.models import Category
from reviews.models import Genre
from reviews.models import Title


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
