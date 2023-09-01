from django.shortcuts import render
from home.views import Menu
from shop.models import Item


def shop(request):
    menu = Menu.objects.all()
    items = Item.objects.all()
    return render(request, 'shop/shop.html', {'menu': menu, 'items': items})
