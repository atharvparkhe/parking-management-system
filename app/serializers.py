from rest_framework import serializers
from .models import *


class ParkingSlotsSerialzer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSlotsModel
        fields = ["slot_name", "is_occupied"]

class MultiParkingCentersModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingCenterModel
        exclude = ["created_at", "updated_at"]

class ParkingCenterModelSerializer(serializers.ModelSerializer):
    slots = serializers.SerializerMethodField()
    class Meta:
        model = ParkingCenterModel
        exclude = ["created_at", "updated_at"]
    def get_slots(self, obj):
        slots = []
        try:
            parking_obj = ParkingCenterModel.objects.get(id=obj.id)
            ser = ParkingSlotsSerialzer(parking_obj.parking_slot.all(), many=True)
            return ser.data
        except Exception as e:
            print(e)
