from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=5)
    category = models.CharField(max_length=100, default='another')
    length = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    material = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    image = models.ImageField(upload_to='shop/images')
    discount_price = models.CharField(max_length=5, null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
