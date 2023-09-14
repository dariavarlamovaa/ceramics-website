from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('comparison/', views.all_items_for_comparison, name='comparison'),
    path('add-comparison-item/<str:pk>', views.add_item_to_comparison, name='add-to-compare'),
    path('delete-comparison-item/<str:pk>', views.delete_item_from_comparison, name='delete-compare-item')

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
