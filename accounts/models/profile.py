from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    avatar = models.ImageField(upload_to='avatars', blank=True)
    bio = models.TextField(max_length=500, blank=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
