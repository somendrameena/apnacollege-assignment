from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


class Chapter(models.Model):
    name = models.CharField(max_length=100)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.topic.name+ " - " + self.name


class Question(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
