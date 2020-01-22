from rest_framework import serializers
from django.conf import settings
from django.contrib.auth import get_user_model
from ideas.models import Idea
from joins.models import Join
from ideas.serializer import IdeaSerializer
from joins.serializer import JoinSerializer

class UserSerializer(serializers.ModelSerializer):

    ideas = IdeaSerializer(many=True, read_only=True, source="idea_set")
    joins = JoinSerializer(many=True, read_only=True, source="join_set")

    class Meta:
        User = get_user_model()
        model = User
        fields = ('username', 'email', 'password','ideas', 'joins')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance