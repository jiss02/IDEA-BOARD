from rest_framework import serializers
from django.conf import settings 
from .models import Join
from ideas.models import Idea
from django.contrib.auth import get_user_model

class JoinSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset=get_user_model().objects.all(),slug_field='username')
    idea = serializers.SlugRelatedField(queryset=Idea.objects.all(),slug_field='name')
    class Meta:
        model = Join
        fields = ('user', 'idea')