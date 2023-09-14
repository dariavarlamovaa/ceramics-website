from django.db import models
from django.contrib.auth.models import User
from shop.models import Item


class Favourite(models.Model):
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=5)
    image = models.ImageField(upload_to='favourites/images')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    main_item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
