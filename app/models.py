from django.db import models
from base.models import *

class ParkingCenterModel(BaseModel):
    name = models.CharField(max_length=50)
    lattitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    def __str__(self):
        return self.name
    

class ParkingSlotsModel(BaseModel):
    slot_name = models.CharField(max_length=50)
    is_occupied = models.BooleanField(default=False)
    parking = models.ForeignKey(ParkingCenterModel, related_name="parking_slot", on_delete=models.CASCADE)
    def __str__(self):
        return self.slot_name
    
