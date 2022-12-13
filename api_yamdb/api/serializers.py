from rest_framework import serializers

from reviews.models import Category
from reviews.models import Genre
from reviews.models import Title


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для модели Category."""

    class Meta:
        model = Category
        exclude = ("id",)


class GenreSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Genre."""

    class Meta:
        model = Genre
        exclude = ("id",)


class TitleSerializerGET(serializers.ModelSerializer):
    """Сериализатор для модели Title при GET запросе."""
    genre = GenreSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    rating = serializers.IntegerField(required=False)

    class Meta:
        model = Title
        fields = (
            "id",
            "name",
            "year",
            "rating",
            "description",
            "genre",
            "category"
        )
        read_only_fields = ("__all__",)


class TitleSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Title при остальных запросах."""
    genre = serializers.SlugRelatedField(
        many=True,
        slug_field="slug",
        queryset=Genre.objects.all()
    )
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field="slug"
    )

    class Meta:
        model = Title
        fields = (
            "name",
            "year",
            "description",
            "genre",
            "category"
        )
