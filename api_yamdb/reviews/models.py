from django.db import models


class Category(models.Model):
    """Модель категорий."""
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    """Модель жанры."""
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Title(models.Model):
    """Модель произведений."""
    name = models.CharField(max_length=256)
    year = models.IntegerField()
    description = models.TextField(
        blank=True,
        null=True
    )
    genre = models.ManyToManyField(
        Genre,
        through="TitleGenre"
    )
    category = models.ForeignKey(
        Category,
        related_name="title",
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name


class TitleGenre(models.Model):
    """Связующая модель для поля жанр."""
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} {self.genre}"
