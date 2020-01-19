from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
    path('', views.usersAssign.as_view()),
    path('signup/', views.usersAssign.as_view()),
    path('login/', views.usersLogin),
]