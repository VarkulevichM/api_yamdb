from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.core.mail import EmailMessage


class User(AbstractUser):
    """Пользователь."""

    role = models.SlugField(max_length=20, default="user")
    bio = models.TextField(
        max_length=200,
        blank=True,
    )
    confirmation_code = models.UUIDField(unique=True, default=uuid.uuid4)


@receiver(pre_save, sender=User)
def staff2admin(sender, **kwargs):
    """Перед созранением, если это staff, то меняем ему роль на admin."""
    user = kwargs.get("instance")
    if user:
        if user.is_staff:
            user.role = "admin"


@receiver(post_save, sender=User)
def after_create_user(sender, **kwargs):
    """После сохранения пользователя отправляем по почте confirmation_code."""
    user = kwargs.get("instance")
    if user:
        email = EmailMessage(
            f"confirmation_code for user {user.username}",
            str(user.confirmation_code),
            user.email,
            [user.email],
        )
        email.send()
