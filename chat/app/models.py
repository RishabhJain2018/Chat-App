from __future__ import unicode_literals
from django.db import models


class Room(models.Model):
    name = models.TestField()
    label = models.SlugField(unique=True)


class Message(models.Model):
    room = models.ForeignKey(Room, related_name="messages")
    handle = models.TextField()
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, sb_index=True)
