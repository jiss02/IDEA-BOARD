from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views as authviews
from . import views

urlpatterns = [
    path('', views.usersAssign.as_view()),
    path('signup/', views.usersAssign.as_view()),
    path('api-token-auth/', authviews.obtain_auth_token),
]