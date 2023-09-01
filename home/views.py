from django.shortcuts import render
from .models import Menu



def home(request):
    menu = Menu.objects.all()
    return render(request, 'home/home.html', {'menu': menu})

