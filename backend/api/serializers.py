"""Serializers for the Taski API.

This module defines serializers for converting model instances to JSON.
"""

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for the Task model."""

    class Meta:
        """Metadata for the TaskSerializer."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
