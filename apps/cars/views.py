from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import CarModel
from .serializers import CarSerializer

# CRUD
"""
Create POST
Read GET
Update PATCH PUT
Delete DELETE
"""


class CarListCreateView(ListCreateAPIView):
    # queryset = CarModel.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        qs = CarModel.objects.all()
        price_lt = self.request.query_params.get('price_lt', None)
        if price_lt:
            qs = qs.filter(price__lt=price_lt)
        auto_park_id = self.request.query_params.get('auto_park', None)
        if auto_park_id:
            qs = qs.filter(auto_park=auto_park_id)
        return qs

class ReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer