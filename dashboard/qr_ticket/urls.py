from django.urls import path

from .views import *

urlpatterns = [
    path('source/', source, name='source'),
    path('destination/', destination, name='destination')
]