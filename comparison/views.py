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
    comparison_count = Comparison.objects.filter(user=request.user).count()
    max_comparison_count = 3
    if comparison_count < max_comparison_count:
        comparison, created = Comparison.objects.get_or_create(
            main_item=item,
            title=item.title,
            price=item.price,
            type=item.type,
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
