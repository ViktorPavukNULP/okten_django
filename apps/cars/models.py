from django.db import models
from django.core import validators as V

from apps.autopark.models import AutoParkModel


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'
        verbose_name = 'Car'

    brand = models.CharField(max_length=30)
    price = models.IntegerField(validators=(V.MinValueValidator(1000), V.MaxValueValidator(100000)))
    year = models.IntegerField(validators=(V.MinValueValidator(1900), V.MaxValueValidator(2022)))
    auto_park = models.ForeignKey(AutoParkModel,on_delete=models.CASCADE, related_name='cars')