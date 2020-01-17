from rest_framework import serializers
from .models import Idea

class IdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idea
        fields = ('id', 'name', 'detail')
        read_only_fields = ('writer', 'created_date', 'updated_date')