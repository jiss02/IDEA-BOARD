from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
    path('', views.IdeaList.as_view()),
    path('<int:pk>/', views.IdeaDetail.as_view()),
]