from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    FARMER = "farmer"
    AGRICULTURIST = "agriculturist"

    ROLE_CHOICES = [
        (FARMER, "Farmer"),
        (AGRICULTURIST, "Agriculturist"),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )

    phone_number = models.CharField(
        max_length=20,
        blank=True
    )

    def __str__(self):
        return self.username

    def __str__(self):
        return self.username