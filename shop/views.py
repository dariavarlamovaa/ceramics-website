from django.shortcuts import render, get_object_or_404, redirect
from home.views import Menu
from shop.models import Item
from .forms import ItemForm


def shop(request):
    menu = Menu.objects.all()
    items = Item.objects.all()
    return render(request, 'shop/shop.html', {'menu': menu, 'items': items})


def additem(request):
    if request.method == 'GET':
        return render(request, 'shop/add_item.html', {'form': ItemForm()})
    else:
        try:
            form = ItemForm(request.POST, request.FILES)
            new_item = form.save(commit=True)
            # new_product.user = request.user
            new_item.save()
            return redirect('shop')
        except ValueError:
            return render(request, 'shop/add_item.html',
                          {'form': ItemForm(),
                           'error': 'Invalid input'})


def viewitem(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)
    form = ItemForm(instance=item)
    if request.method == 'GET':
        return render(request, 'shop/viewitem.html', {'item': item, 'form': form})
    else:
        try:
            form = ItemForm(request.POST, instance=item)
            form.save()
            return redirect('shop')
        except ValueError:
            return render(request, 'shop/viewitem.html', {'form': form, 'error': 'Invalid data'})


def deleteitem(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)
    if request.method == 'POST':
        item.delete()
        return redirect('shop')
