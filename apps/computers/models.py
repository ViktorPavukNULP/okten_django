from django.db import models

class ComputerModel(models.Model):
    class Meta:
        db_table = 'computers'
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    ram = models.IntegerField()
    display_size = models.FloatField()
