import datetime

from django.shortcuts import render, get_object_or_404, redirect
from home.views import Menu
from shop.models import Item
from .forms import ItemForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone


def shop(request):
    menu = Menu.objects.all()
    items = Item.objects.all()
    sort_by = request.GET.get('sort_by')
    category = request.GET.get('category')
    categories = Item.objects.values_list('category', flat=True).distinct()
    now = timezone.now()
    if sort_by:
        items = Item.objects.order_by(sort_by).all()
        context = {'items': items, 'menu': menu, 'categories': categories, 'now': now}
        return render(request, 'shop/shop.html', context)
    if category:
        items = Item.objects.filter(category=category).all()
        context = {'items': items, 'menu': menu, 'categories': categories, 'now': now}
        return render(request, 'shop/shop.html', context)
    if 'discount_items' in request.GET:
        items = Item.objects.filter(discount_price__isnull=False, start_date__lte=now, end_date__gte=now)

    return render(request, 'shop/shop.html', {'menu': menu, 'items': items, 'categories': categories, 'now': now})


@login_required
def add_item(request):
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


@login_required
def edit_item(request, item_pk):
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


@login_required
def delete_item(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)
    if request.method == 'POST':
        item.delete()
        return redirect('shop')


def view_one_item(request, item_pk):
    menu = Menu.objects.all()
    one_item = Item.objects.get(pk=item_pk)
    return render(request, 'shop/single_item.html', {'item': one_item, 'menu': menu})
