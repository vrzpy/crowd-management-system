from django import views
from django.urls import path

from .views import *

urlpatterns = [
    path('station-status',StationStatus,name="StationStatus"),
    path('update-news',UpdateNews,name="UpdateNews"),
]