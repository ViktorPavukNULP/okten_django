from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from ..profile.serializers import AddAvatarSerializer
from .permissions import IsSuperUser
from .serializers import UserSerializer

UserModel = get_user_model()


class UserListCreateView(ListCreateAPIView):

    def get_permissions(self):
        if self.request.method == 'POST':
            return (AllowAny(),)
        return super().get_permissions()

    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class UserToAdminView(GenericAPIView):
    permission_classes = (IsSuperUser,)
    queryset = UserModel.objects.all()

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_staff:
            return Response({"detail": "User is already an admin"}, status=status.HTTP_400_BAD_REQUEST)
        user.is_staff = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AdminToUserView(GenericAPIView):
    permission_classes = (IsSuperUser,)
    queryset = UserModel.objects.all()

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_staff:
            return Response({"detail": "User is already not an admin"}, status=status.HTTP_400_BAD_REQUEST)
        user.is_staff = False
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AddAvatarView(UpdateAPIView):
    serializer_class = AddAvatarSerializer

    def get_object(self):
        return self.request.user.profile



