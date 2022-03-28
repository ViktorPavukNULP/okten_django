from django.contrib.auth import get_user_model

from rest_framework.serializers import ModelSerializer

UserModel = get_user_model()


class UserSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'password', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'created_at', 'updated_at'
        )
        read_only_fields = (
            'id', 'is_active', 'is_staff', 'is_superuser', 'is_active', 'last_login', 'created_at', 'updated_at'
        )

        write_only_fields = ('password',)
