from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from home.models import Menu
from shop.models import Item
from .models import Favourite


def favourites(request):
    menu = Menu.objects.all()
    all_favourites = Favourite.objects.filter(user=request.user)
    return render(request, 'favourites/favourites.html', {'menu': menu, 'all_favourites': all_favourites})


@login_required
def add_to_favourites(request, pk):
    item = get_object_or_404(Item, pk=pk)
    favourite, created = Favourite.objects.get_or_create(
        main_item=item,
        title=item,
        price=item.price,
        image=item.image,
        user=request.user
    )
    if not created:
        favourite.save()
    return redirect('shop')


@login_required
def delete_favourite(request, pk):
    favourite = get_object_or_404(Favourite, id=pk, user=request.user)
    if request.method == 'GET':
        favourite.delete()
        return redirect('favourites')


@login_required
def clear_favourites(request):
    all_favourites = Favourite.objects.filter(user=request.user)
    if request.method == 'GET':
        all_favourites.delete()
        return redirect('favourites')