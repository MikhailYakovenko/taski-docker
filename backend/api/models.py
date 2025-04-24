"""Database models for the Taski API.

This module defines the data models used in the Taski application.
"""
from django.db import models


class Task(models.Model):
    """Model representing a task in the Taski application."""

    title = models.CharField(verbose_name='Заголовок', max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title
