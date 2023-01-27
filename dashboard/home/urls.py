from django.urls import path

from .views import *

urlpatterns = [
    path('', home_index, name='home_index'),
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('register/', registerUser, name='register'),
]