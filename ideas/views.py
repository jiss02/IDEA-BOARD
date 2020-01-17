from django.shortcuts import render
from rest_framework import viewsets
from .serializer import IdeaSerializer
from .models import Idea

class IdeaViewSet(viewsets.ModelViewSet):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer
