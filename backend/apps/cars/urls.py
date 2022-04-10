from django.urls import path

from .views import CarListCreateView, ReadUpdateDeleteView

urlpatterns = [
    path('', CarListCreateView.as_view(), name='cars_list_create'),
    path('<int:pk>/', ReadUpdateDeleteView.as_view(), name='cars_read_update_delete')
]

# localhost:8000/cars