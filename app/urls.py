from django.urls import path
from . import views
from .views import *

urlpatterns = [
	path('all-parking-centers/', views.AllParkingCentersView.as_view(), name="all-parking-centers"),
	path('single-parking-center/<id>/', views.SingleParkingCenterView.as_view(), name="single-parking-centers"),
]