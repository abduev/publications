from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    AUTHOR = 'author'
    FOLLOWER = 'follower'
    ROLES_CHOICES = [
        (AUTHOR, 'Author'),
        (FOLLOWER, 'Follower')
    ]

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    username = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, unique=True)
    role = models.CharField(
        max_length=10, choices=ROLES_CHOICES, default=FOLLOWER,
    )
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    @property
    def is_author(self):
        return self.role == self.AUTHOR or self.is_staff

    @property
    def is_follower(self):
        return self.role == self.FOLLOWER
