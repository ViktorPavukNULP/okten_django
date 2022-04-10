from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from .filters import CarFilter
from .models import CarModel
from .serializers import CarSerializer, CarSerializerAutopark
from pagination.default_pagination import DefaultPagination
# CRUD
"""
Create POST
Read GET
Update PATCH PUT
Delete DELETE
"""


class CarListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = CarModel.objects.all()
    serializer_class = CarSerializerAutopark
    filterset_class = CarFilter


class ReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer