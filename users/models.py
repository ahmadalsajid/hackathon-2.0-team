from django.db import models


class Video(models.Model):
    video_url = models.CharField(max_length=500, unique=True)
    video_caption = models.TextField(null=True, blank=True)
    author_username = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tiktoker(models.Model):
    username = models.CharField(max_length=100, unique=True)
    following_count = models.IntegerField(default=0)
    followers_count = models.IntegerField(default=0)
    likes_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
