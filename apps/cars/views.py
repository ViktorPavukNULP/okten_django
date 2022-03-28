from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CarModel
from .serializers import CarSerializer, CarSerializerAutopark

# CRUD
"""
Create POST
Read GET
Update PATCH PUT
Delete DELETE
"""


class CarListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = CarSerializerAutopark

    def get_queryset(self):
        qs = CarModel.objects.all()
        price_lt = self.request.query_params.get('price_lt', None)
        if price_lt:
            qs = qs.filter(price__lt=price_lt)
        auto_park_id = self.request.query_params.get('auto_park_id', None)
        if auto_park_id:
            qs = qs.filter(auto_park=auto_park_id)
        return qs

class ReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer