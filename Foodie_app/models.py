from django.db import models

# Create your models here.

class Posts(models.Model):
    user_post = models.TextField(max_length=300)
    user_restaurant = models.CharField(max_length=150)
    user_image = models.ImageField()
    