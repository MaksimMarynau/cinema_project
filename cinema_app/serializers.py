from rest_framework import serializers

from . import models


class MovieListSerializer(serializers.ModelSerializer):
    """List of movies"""

    class Meta:
        model = models.Movie
        fields = ("title", "price")

class MovieDetailSerializer(serializers.ModelSerializer):
    """Description all movie"""

    class Meta:
        model = models.Movie
        fields = "__all__"

class TicketSerializer(serializers.ModelSerializer):
    """Tickets"""

    class Meta:
        model = models.Ticket
        fields = "__all__"
