from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=5)
    type = models.CharField(max_length=100, default='another')
    length = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    material = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    image = models.ImageField(upload_to='shop/images')
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
