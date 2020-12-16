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
    """Information about ticket"""

    movie = serializers.SlugRelatedField(slug_field='title',read_only=True)
    

    class Meta:
        model = models.Ticket
        fields = ('id','amount','movie','ip')

class BuyTicketSerializer(serializers.ModelSerializer):
    """Form to buy a ticket"""

    class Meta:
        model = models.Ticket
        fields = ("amount","movie")

    def buy(self, validated_data):
        ticket = models.Ticket.objects.create(
            ip = validated_data.get('ip', None),
            movie = validated_data.get('movie', None),
            defaults={'amount': validated_data.get('amount')}
        )
        return ticket
