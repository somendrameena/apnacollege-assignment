from django.contrib.auth import get_user_model

from rest_framework import serializers

from api.models import Topic, Chapter, Question

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


class QuestionSerializer(serializers.ModelSerializer):
    chapter = serializers.CharField(source="chapter.name")
    topic = serializers.CharField(source="chapter.topic.name")

    class Meta:
        model = Question
        fields = ['id', 'title', 'chapter', 'topic', 'created']


class QuestionDetailSerializer(serializers.ModelSerializer):
    topic = serializers.SerializerMethodField()

    def get_topic(self, instance):
        return instance.chapter.topic.name+ " - " + instance.chapter.name

    class Meta:
        model = Question
        fields = ['id', 'title', 'topic', 'created', 'content']