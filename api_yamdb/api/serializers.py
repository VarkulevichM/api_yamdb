from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from reviews.models import Category, Comment, Genre, Review, Title

User = get_user_model()


class ReviewSerializer(serializers.ModelSerializer):
    title = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True
    )
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    def validate_score(self, value):
        if 0 > value > 10:
            raise serializers.ValidationError('Оценка по 10-бальной шкале!')
        return value

    def validate_rewiews_count(self, data):
        request = self.context['request']
        author = request.user
        title_id = self.context.get('view').kwargs.get('title_id')
        title = get_object_or_404(Title, id=title_id)
        if request.method == 'POST' \
           and Review.objects.filter(title=title, author=author).exists():
           raise ValidationError('Может существовать только один отзыв!')
        return data


    class Meta:
        model = Review
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    review = serializers.SlugRelatedField(
        slug_field='text',
        read_only=True
    )
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Comment
        fields = '__all__'
        

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
