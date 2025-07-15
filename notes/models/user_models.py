from django.db import models
from django.contrib.auth.models import AbstractUser
from notes.constants.default_value import Gender


class User(AbstractUser):
    username = None  # Completely remove username field
    email = models.EmailField(unique=True)  # This will now act as the username
    password = models.CharField(max_length=128)  # Password field is still required

    name = models.CharField(max_length=120)
    gender = models.IntegerField(
        choices=[(gender.value, gender.name) for gender in Gender],
        null=False, blank=False
    )

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'  # Important
    REQUIRED_FIELDS = []  # Don't include 'username' here

    class Meta:
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}"
