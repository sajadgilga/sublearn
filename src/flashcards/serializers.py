from rest_framework import serializers

from .models import MovieSet


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSet
        # fields=('',)
