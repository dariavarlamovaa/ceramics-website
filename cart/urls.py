from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('add-item-to-cart/<str:pk>/', views.add_to_cart, name='add-item-to-cart'),
    path('delete-item/<str:pk>/', views.delete_item, name='delete-item'),
    path('update-cart/', views.update_cart, name='update-cart'),
    path('checkout/', views.checkout, name='checkout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)