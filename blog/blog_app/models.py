from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    @staticmethod
    def get_absolute_url():
        return reverse("home")


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=4048)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(default=timezone.now)

    @staticmethod
    def get_absolute_url():
        return reverse("home")


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like_status = models.BooleanField(default=True)
    dislike_status = models.BooleanField(default=False)
