from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('shop/', views.shop, name='shop'),
    path('item/editing-item/<int:item_pk>', views.edit_item, name='edit-item'),
    path('item/<int:item_pk>/delete', views.delete_item, name='delete'),
    path('add-item/', views.add_item, name='additem'),
    path('item/<int:item_pk>', views.view_one_item, name='view-item'),
    path('', include('cart.urls')),
    path('', include('comparison.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
