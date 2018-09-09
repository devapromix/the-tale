
from django.db import models

from django.contrib.postgres import fields as postgres_fields


class Event(models.Model):

    id = models.BigAutoField(primary_key=True)

    data = postgres_fields.JSONField(default='{}')

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    created_at_turn = models.BigIntegerField(db_index=True)

    class Meta:
        db_table = 'events'


class Tag(models.Model):

    id = models.BigAutoField(primary_key=True)

    object_type = models.BigIntegerField()

    object_id = models.BigIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    created_at_turn = models.BigIntegerField()

    class Meta:
        db_table = 'tags'
        unique_together = (('object_type', 'object_id'),)


class EventTag(models.Model):

    id = models.BigAutoField(primary_key=True)

    event = models.ForeignKey(Event)

    tag = models.ForeignKey(Tag, db_index=True)

    class Meta:
        db_table = 'events_tags'
