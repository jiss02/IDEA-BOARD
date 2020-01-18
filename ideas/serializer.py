from rest_framework import serializers
from .models import Idea
from django.contrib.auth.models import User 

class IdeaSerializer(serializers.ModelSerializer):
    
    writer = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=True)

    class Meta:
        model = Idea
        fields = ('writer', 'name', 'detail','created_date', 'updated_date', 'views')
        read_only_fields = ('writer', 'created_date', 'updated_date', 'views')
