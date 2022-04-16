from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

from ..profile.serializers import AddAvatarSerializer
from .permissions import IsSuperUser
from .serializers import UserSerializer

UserModel = get_user_model()


class UserListCreateView(ListCreateAPIView):

    def get_permissions(self):
        if self.request.method == 'POST':
            return AllowAny(),
        return IsAdminUser(),

    def get_queryset(self):
        qs = UserModel.objects.all()
        return qs.exclude(id=self.request.user.id)

    serializer_class = UserSerializer


class UserToAdminView(GenericAPIView):
    permission_classes = (IsSuperUser,)
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

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
    serializer_class = UserSerializer

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_staff:
            return Response({"detail": "User is already not an admin"}, status=status.HTTP_400_BAD_REQUEST)
        user.is_staff = False
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ActivateUserView(GenericAPIView):
    permission_classes = (IsAdminUser,)
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_superuser and user.is_staff:
            return Response({"detail": "You do not have permission to perform this action with admins"}, status=status.HTTP_400_BAD_REQUEST)
        if user.is_active:
            return Response({"detail": "User is already active"}, status=status.HTTP_400_BAD_REQUEST)
        user.is_active = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeactivateUserView(GenericAPIView):
    permission_classes = (IsAdminUser,)
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_superuser or user.is_staff:
            return Response({"detail": "You do not have permission to perform this action with admins"}, status=status.HTTP_400_BAD_REQUEST)
        if not user.is_active:
            return Response({"detail": "User is already deactivated"}, status=status.HTTP_400_BAD_REQUEST)
        user.is_active = False
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AddAvatarView(UpdateAPIView):
    serializer_class = AddAvatarSerializer

    def get_object(self):
        return self.request.user.profile

