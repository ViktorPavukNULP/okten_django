from django_filters import rest_framework as filters

from .models import CarModel


class CarFilter(filters.FilterSet):
    price = filters.RangeFilter()
    brand_start = filters.CharFilter(field_name='brand', lookup_expr='istartswith')

    class Meta:
        model = CarModel
        fields = ('id', 'price', 'brand_start')
