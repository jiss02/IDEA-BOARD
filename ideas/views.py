from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from .serializer import IdeaSerializer
from .models import Idea
from datetime import datetime

class IdeaViewSet(viewsets.ModelViewSet):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer

    def perform_create(self, serializer):
        serializer.save(writer=self.request.user)
