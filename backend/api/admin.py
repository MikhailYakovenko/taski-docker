"""Admin configuration for the Taski API.

This module defines the admin interface for the API models.
"""

from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Admin interface for the Task model."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
