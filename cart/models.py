from django.db import models
from django.contrib.auth.models import User
from shop.models import Item


class Cart(models.Model):
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=5)
    image = models.ImageField(upload_to='cart/images')
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    main_item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Purchase(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=500)
    address = models.TextField(max_length=100)
    city = models.TextField(max_length=50)
    postcode = models.TextField(max_length=50)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstname
