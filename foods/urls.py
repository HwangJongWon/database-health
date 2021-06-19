from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   
    path('fit/', views.index),
    path('fit/<int:pk>/', views.health_detail)
]

