from django.shortcuts import render, get_object_or_404, redirect
from .models import Comparison
from home.models import Menu
from shop.models import Item
from django.contrib.auth.decorators import login_required


def all_items_for_comparison(request):
    menu = Menu.objects.all()
    compared_items = Comparison.objects.filter(user=request.user)
    return render(request, 'comparison/comparison.html', {'compared_items': compared_items, 'menu': menu})


@login_required
def add_item_to_comparison(request, pk):
    item = get_object_or_404(Item, pk=pk)
    maximum_items_number = 5
    user_comparisons = Comparison.objects.filter(user=request.user)
    if user_comparisons.count() < 5:
        comparison, created = Comparison.objects.get_or_create(
            main_item=item,
            title=item.title,
            price=item.price,
            category=item.category,
            length=item.length,
            height=item.height,
            weight=item.weight,
            material=item.material,
            color=item.color,
            image=item.image,
            user=request.user
        )
        if not created:
            comparison.save()
    return redirect('shop')


@login_required
def delete_item_from_comparison(request, pk):
    compared_item = get_object_or_404(Comparison, pk=pk, user=request.user)
    if request.method == 'GET':
        compared_item.delete()
        return redirect('comparison')
