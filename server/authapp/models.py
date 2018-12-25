from django.db import models
from django.contrib.auth.models import AbstractUser

class ShopUser(AbstractUser):
    avatar = models.ImageField(
        upload_to='user_avatars',
        blank=True,
        null=True
    )
    age = models.PositiveIntegerField(
        verbose_name='возраст',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.username
