from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import JoinSerializer
from .models import Join

@api_view(['POST'])
def joinCreate(req):
    try:
        serializer = JoinSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    except Exception as err:
        print(err)
        return Response("에러발생 터미널을 확인하십시오", status=500)

@api_view(['DELETE'])
def joinDelete(req, pk):
    try:
        join = get_object_or_404(Join, pk=pk)
        join.delete()
        return Response("삭제 성공")
    except Exception as err:
        print(err)
        return Response("에러발생 터미널을 확인하십시오", status=500)


