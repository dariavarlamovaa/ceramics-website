from django.shortcuts import render, get_object_or_404, redirect
from home.views import Menu
from shop.models import Item
from .forms import ItemForm


def shop(request):
    menu = Menu.objects.all()
    items = Item.objects.all()
    return render(request, 'shop/shop.html', {'menu': menu, 'items': items})


def additem(request):
    menu = Menu.objects.all()
    if request.method == 'GET':
        return render(request, 'shop/add_item.html', {'form': ItemForm(), 'menu': menu})
    else:
        try:
            form = ItemForm(request.POST, request.FILES)
            new_item = form.save(commit=True)
            # new_product.user = request.user
            new_item.save()
            return redirect('shop')
        except ValueError:
            return render(request, 'shop/add_item.html',
                          {'form': ItemForm(), 'menu': menu,
                           'error': 'Invalid input'})


def viewitem(request, item_pk):
    menu = Menu.objects.all()
    item = get_object_or_404(Item, pk=item_pk)
    form = ItemForm(instance=item)
    if request.method == 'GET':
        return render(request, 'shop/item.html', {'item': item, 'form': form, 'menu': menu})
    else:
        try:
            form = ItemForm(request.POST, instance=item)
            form.save()
            return redirect('shop')
        except ValueError:
            return render(request, 'shop/item.html', {'form': form, 'menu': menu, 'error': 'Invalid data'})


def deleteitem(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)
    if request.method == 'POST':
        item.delete()
        return redirect('shop')


def sort_items(request):
    menu = Menu.objects.all()
    sort_by = request.GET.get('sort_by')
    print(f"Sorting by: {sort_by}")
    items = Item.objects.all()
    if sort_by == 'price':
        items = Item.objects.order_by('price')
    elif sort_by == 'type':
        items = Item.objects.order_by('type')
    elif sort_by == 'title':
        items = Item.objects.order_by('title')

    context = {'items': items, 'menu': menu}

    return render(request, 'shop/shop.html', context)
