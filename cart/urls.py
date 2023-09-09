from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('add-item-to-cart/<str:pk>/', views.addtocart, name='add-item-to-cart'),
    path('delete-item/<str:pk>/', views.item_clear, name='delete-item'),
    path('update-cart/', views.update_cart, name='update-cart')

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)