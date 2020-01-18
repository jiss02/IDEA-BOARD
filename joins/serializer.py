from rest_framework import serializers
from django.contrib.auth.models import User 
from .models import Join
from ideas.models import Idea

class JoinSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=True)
    idea = serializers.PrimaryKeyRelatedField(queryset=Idea.objects.all(), required=True)

    class Meta:
        model = Join
        fields = ('user', 'idea')