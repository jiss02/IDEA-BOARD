from django.shortcuts import get_object_or_404
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserSerializer
from hackIdea.permissions import UserPermission
# 에러
from hackIdea import errors
# 로직
class usersAssign(APIView):
    
    permission_classes = (UserPermission,)

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
            eights = ["지현이","이주형","최정연", "유지연"]
            if req.data["username"] not in eights:
                raise errors.NotEights
            serializer = UserSerializer(data=req.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except errors.NotEights:
            return Response("8기 멋사 구성원이 아닙니다")
        except Exception as err:
            print(err)
            return Response("에러발생 터미널을 확인하십시오", status=500)

