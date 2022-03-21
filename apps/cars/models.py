from django.db import models


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'
        verbose_name = 'Car'

    brand = models.CharField(max_length=30)
    price = models.IntegerField()
    year = models.IntegerField()