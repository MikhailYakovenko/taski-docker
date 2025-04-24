"""Application configuration for the Taski API.

This module defines the configuration for the API Django app.
"""

from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Configuration for the API app."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
