from rest_framework import serializers
from .models import Idea

class IdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idea
        fields = ('writer','name', 'detail','created_date', 'updated_date', 'views')
        read_only_fields = ('writer','created_date', 'updated_date', 'views')