from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('shop/', views.sort_items, name='shop'),
    path('item/<int:item_pk>', views.viewitem, name='viewitem'),
    path('item/<int:item_pk>/delete', views.deleteitem, name='delete'),
    path('add_item/', views.additem, name='additem'),
    path('', include('cart.urls')),
    path('sort_items/', views.sort_items, name='sort_items'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
