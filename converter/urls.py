from django.urls import path
from . import views

urlpatterns = [
    path('', views.length_converter, name='home'),  # Zmieniono z views.home na views.length_converter
    path('length/', views.length_converter, name='length_converter'),
    path('weight/', views.weight_converter, name='weight_converter'),
    path('temperature/', views.temperature_converter, name='temperature_converter'),
]
