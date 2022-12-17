from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
from django.dispatch import receiver
from django.db.models.signals import pre_save


class User(AbstractUser):
    """Пользователь."""

    role = models.SlugField(max_length=20, default="user")
    bio = models.TextField(
        max_length=200,
        blank=True,
    )
    confirmation_code = models.UUIDField(unique=True, default=uuid.uuid4)

    class Meta(object):
        unique_together = ("email",)


@receiver(pre_save, sender=User)
def staff2admin(sender, **kwargs):
    """Перед созранением, если это staff, то меняем ему роль на admin."""
    user = kwargs.get("instance")
    if user:
        if user.is_staff:
            user.role = "admin"
