from rest_framework.serializers import ModelSerializer

from .models import ComputerModel


class ComputerSerializer(ModelSerializer):
    class Meta:
        model = ComputerModel
        fields = ('id', 'model', 'brand', 'ram', 'display_size')
