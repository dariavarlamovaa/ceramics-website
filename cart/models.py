from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum



class Cart(models.Model):
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=5)
    image = models.ImageField(upload_to='cart/images')
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


