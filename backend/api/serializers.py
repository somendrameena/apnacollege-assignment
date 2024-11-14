from django.contrib.auth import get_user_model

from rest_framework import serializers

from api.models import Topic, Chapter

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'name']


class ChapterSerializer(serializers.ModelSerializer):
    topic = serializers.CharField(source="topic.name")

    class Meta:
        model = Chapter
        fields = ['id', 'name', 'topic']