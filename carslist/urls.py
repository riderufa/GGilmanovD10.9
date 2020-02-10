from django.contrib import admin
from django.urls import path

from carslist.views import CarListView

app_name = 'carslist'
urlpatterns = [
    path('', CarListView.as_view(), name='car_list'),
]
