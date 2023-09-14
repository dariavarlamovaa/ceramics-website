from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('favourites/', views.favourites, name='favourites'),
    path('add-to-favourites/<str:pk>', views.add_to_favourites, name='add-to-favourites'),
    path('delete-favourite/<str:pk>', views.delete_favourite, name='delete-favourite'),
    path('clear-favourites/', views.clear_favourites, name='clear-favourites'),
    path('', include('shop.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
