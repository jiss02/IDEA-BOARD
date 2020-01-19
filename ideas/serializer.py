from rest_framework import serializers
from .models import Idea
from django.conf import settings 
from django.contrib.auth import get_user_model
from joins.models import Join
from joins.serializer import JoinSerializer
class IdeaSerializer(serializers.ModelSerializer):
    writer = serializers.SlugRelatedField(read_only=True, slug_field="username")
    joins = JoinSerializer(many=True, read_only=True, source="join_set")
    class Meta:
        model = Idea
        fields = ('writer', 'name', 'detail','created_date', 'updated_date', 'views', 'joins')
        read_only_fields = ('writer', 'created_date', 'updated_date', 'views', 'joins')
