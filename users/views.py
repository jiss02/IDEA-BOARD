from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
# from .serializer import UserSerializer
# from .models import User

# Create your views here.
class UserTempClass(APIView):
    def get(self, req):
        return Response("something")