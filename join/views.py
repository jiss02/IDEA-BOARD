from django.shortcuts import render
from rest_framework import viewsets
from .serializer import JoinSerializer
from .models import Join

# Create your views here.
class JoinViewSet(viewsets.ModelViewSet):
    queryset = Join.objects.all()
    serializer_class = JoinSerializer