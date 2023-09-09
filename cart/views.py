from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from shop.models import Item
from .models import Cart
from home.models import Menu
from django.db.models import Sum, ExpressionWrapper, F, DecimalField


def cart(request):
    menu = Menu.objects.all()
    cart_items = Cart.objects.filter(user=request.user)
    total = cart_items.aggregate(total_price=Sum(ExpressionWrapper(
        F('price') * F('quantity'),
        output_field=DecimalField(),
    )))
    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'menu': menu, 'total': total['total_price']})


@login_required
def addtocart(request, pk):
    item = get_object_or_404(Item, pk=pk)
    added_item, created = Cart.objects.get_or_create(
        title=item,
        price=item.price,
        image=item.image,
        user=request.user
    )
    if not created:
        added_item.quantity += 1
        added_item.save()
    return redirect('shop')


@login_required
def item_clear(request, pk):
    item = get_object_or_404(Cart, pk=pk, user=request.user)
    if request.method == 'GET':
        item.delete()
        return redirect('cart')


@login_required
def update_cart(request):
    if request.method == "POST":
        item_id = request.POST['item_id']
        new_quantity = int(request.POST['quantity'])
        cart_item = Cart.objects.get(id=item_id)
        cart_item.quantity = new_quantity
        cart_item.save()
        return redirect('cart')
