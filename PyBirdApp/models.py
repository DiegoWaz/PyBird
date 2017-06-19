from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    post_content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="created")
    updated_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="updated")

class Follow(models.Model):
    id = models.IntegerField(primary_key=True)
    id_follower = models.IntegerField()
    id_followed = models.IntegerField()
    post_content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="created")
    updated_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="updated")

    def __str__(self):
        return self.id