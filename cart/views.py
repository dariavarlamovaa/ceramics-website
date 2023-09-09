from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from shop.models import Item
from .models import Cart, Purchase
from home.models import Menu
from django.db.models import Sum, ExpressionWrapper, F, DecimalField
from .forms import PurchaseForm


def cart(request):
    menu = Menu.objects.all()
    cart_items = Cart.objects.filter(user=request.user)
    total = cart_items.aggregate(total_price=Sum(ExpressionWrapper(
        F('price') * F('quantity'),
        output_field=DecimalField(),
    )))
    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'menu': menu, 'total': total['total_price']})


@login_required
def add_to_cart(request, pk):
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
def delete_item(request, pk):
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


@login_required
def checkout(request):
    menu = Menu.objects.all()
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.quantity * int(item.price.split('$')[0]) for item in cart_items)

    if request.method == 'POST':
        form = PurchaseForm(request.POST)

        if form.is_valid():
            new_purchase = form.save(commit=False)
            new_purchase.user = request.user
            new_purchase.total_price = total_price
            new_purchase.save()

            cart_items.delete()

            return redirect('cart')
    else:
        form = PurchaseForm()
    return render(request, 'cart/checkout.html',
                  {'form': form, 'menu': menu, 'cart_items': cart_items, 'total_price': total_price})
