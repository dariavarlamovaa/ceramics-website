from django.db import models


class Item(models.Model):
    title = models.TextField(max_length=50)
    price = models.CharField(max_length=5)
    type = models.CharField(max_length=100, default='another')
    image = models.ImageField(upload_to='shop/images')
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
