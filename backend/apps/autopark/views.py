from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from apps.cars.serializers import CarSerializer

from ..cars.models import CarModel
from .models import AutoParkModel
from .serializers import AutoParkSerializer


class AutoParkListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
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
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer