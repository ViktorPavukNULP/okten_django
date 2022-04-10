from django.urls import path

from .views import (
    ActivateUserView,
    AddAvatarView,
    AdminToUserView,
    DeactivateUserView,
    UserListCreateView,
    UserToAdminView,
)

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user_list_create'),
    path('<int:pk>/admin/',UserToAdminView.as_view(), name='user_set_to_admin'),
    path('<int:pk>/unadmin/',AdminToUserView.as_view(), name='admin_set_to_user'),
    path('<int:pk>/activate/',ActivateUserView.as_view(), name='activate_user'),
    path('<int:pk>/deactivate/',DeactivateUserView.as_view(), name='deactivate_user'),
    path('avatar/', AddAvatarView.as_view(), name='user_add_avatar')

]