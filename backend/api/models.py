from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)


class Chapter(models.Model):
    name = models.CharField(max_length=100)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
