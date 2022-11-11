from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import *
from .models import *


class AllParkingCentersView(ListAPIView):
    queryset = ParkingCenterModel.objects.all()
    serializer_class = MultiParkingCentersModelSerializer


class SingleParkingCenterView(RetrieveAPIView):
    queryset = ParkingCenterModel.objects.all()
    serializer_class = ParkingCenterModelSerializer
    lookup_field = "id"