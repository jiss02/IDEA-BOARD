# Django
from django.shortcuts import render
from django.http import Http404
# DRF
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
# model, serializer import
from .serializer import IdeaSerializer
from .models import Idea
# 파이썬 기본 모듈
from datetime import datetime

class IdeaList(APIView):
    def post(self, req, format=None):
        try:
            serializer = IdeaSerializer(data=req.data)
            if serializer.is_valid():
                serializer.save(writer=req.user)
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except Exception as err:
            print(err)
            return Response("에러발생 터미널을 확인하십시오", status=500)
    def get(self, req, format=None):
        try:
            queryset = Idea.objects.all().order_by('-id')
            serializer = IdeaSerializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as err:
            print(err)
            return Response("에러발생 터미널을 확인하십시오", status=500)

class IdeaDetail(APIView):
    def get_object(self, pk):
        try:
            return Idea.objects.get(pk=pk)
        except Idea.DoesNotExist:
            raise Http404
    def get(self, req, pk):
        try:
            idea = self.get_object(pk)
            idea.views += 1
            idea.save()
            serializer = IdeaSerializer(idea)
            return Response(serializer.data)
        except Http404:
            return Response("없는 아이디어 입니다.", status=404)
        except Exception as err:
            print(err)
            return Response("에러발생 터미널을 확인하십시오", status=500)
    def put(self, req, pk):
        try:
            idea = self.get_object(pk)
            serializer = IdeaSerializer(idea, data=req.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except Http404:
            return Response("없는 아이디어 입니다.", status=404)
        except Exception as err:
            print(err)
            return Response("에러발생 터미널을 확인하십시오", status=500)
    def delete(self, req, pk):
        try:
            idea = self.get_object(pk)
            idea.delete()
            return Response("{}번 글 삭제 완료".format(pk))
        except Http404:
            return Response("없는 아이디어 입니다.", status=404)
        except Exception as err:
            print(err)
            return Response("에러발생 터미널을 확인하십시오", status=500)