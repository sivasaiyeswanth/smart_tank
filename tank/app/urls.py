from django.urls import path
from . import views

urlpatterns = [
    path('', views.tank_status, name='tank_status'),
]
