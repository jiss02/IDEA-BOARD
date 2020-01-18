from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
    path('', views.joinCreate),
    path('<int:pk>/', views.joinDelete)
]