from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
    path('', views.UserTempClass.as_view()),
    path('<int:pk>/', views.UserTempClass.as_view())
]