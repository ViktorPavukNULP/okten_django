from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from .filters import CarFilter
from .models import CarModel
from .serializers import CarSerializer, CarSerializerAutopark
from pagination.default_pagination import DefaultPagination


class CarListCreateView(ListCreateAPIView):
    """
    get:
        Get all cars with filters
    post:
        Create car
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = CarModel.objects.all()
    serializer_class = CarSerializerAutopark
    filterset_class = CarFilter


class ReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """
    get:
        Get Car by id
    put:
        Update car by id
    patch:
        Partial update car by id
    delete:
        Delete car by id
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
