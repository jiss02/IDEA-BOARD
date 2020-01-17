from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from .serializer import IdeaSerializer
from .models import Idea
from datetime import datetime

class IdeaList(APIView):
    def post(self, req, format=None):
        try:
            serializer = IdeaSerializer(data=req.data)
            if serializer.is_valid():
                serializer.updated_date = datetime.now()
                serializer.created_data = datetime.now()
                print(serializer)
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except Exception as err:
            print(err)
            return Response("에러발생 터미널을 확인하십시오")

    def get(self, req, format=None):
        queryset = Idea.objects.all()
        serializer = IdeaSerializer(queryset, many=True)
        print(serializer.data)
        return Response(serializer.data)
