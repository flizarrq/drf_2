from django.db import models

from core.models import BaseModel

from apps.auto_parks.models import AutoParkModel


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=25)
    # brand = models.CharField(unique=True, blank=True, null=True)
    price = models.IntegerField()
    # price = models.IntegerField(default=0)
    year = models.IntegerField()
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')
