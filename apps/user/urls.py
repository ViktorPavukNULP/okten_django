from django.urls import path

from .views import UserListCreateView, UserToAdminView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user_list_create'),
    path('<int:pk>/admin/',UserToAdminView.as_view(), name='user_set_to_admin')

]