from django.shortcuts import get_object_or_404
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserSerializer
# from .models import User

class usersAssign(APIView):
    def get(self, req):
        try:
            User = get_user_model()
            queryset = User.objects.all()
            serializer = UserSerializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as err:
            print(err)
            return Response("에러발생 터미널을 확인하십시오", status=500)
    def post(self, req):
        try:
            return Response(serializer.data)
            return Response(serializer.error)
        except Exception as err:
            print(err)
            return Response("에러발생 터미널을 확인하십시오", status=500)

# 로그인 회원가입 
@api_view(['POST'])
def usersLogin(req):
    return Response("로그인")
