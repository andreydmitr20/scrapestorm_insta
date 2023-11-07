from django.core.validators import (
    RegexValidator,
    EmailValidator,
    MinValueValidator,
    MaxValueValidator,
)
from rest_framework import serializers
from re import match

# from .models import Clients


class EmptySerializer(serializers.Serializer):
    pass
