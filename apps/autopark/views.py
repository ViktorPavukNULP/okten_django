from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.cars.serializers import CarSerializer

from ..cars.models import CarModel
from .models import AutoParkModel
from .serializers import AutoParkSerializer


class AutoParkListCreateView(ListCreateAPIView):
    serializer_class = AutoParkSerializer
    queryset = AutoParkModel.objects.all()


class AutoParkAddCarView(CreateAPIView):
    serializer_class = CarSerializer
    queryset = AutoParkModel.objects.all()

    def perform_create(self, serializer):
        # auto_park_id = self.kwargs.get('pk')
        auto_park = self.get_object()
        serializer.save(auto_park=auto_park)

class AutoParkReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer