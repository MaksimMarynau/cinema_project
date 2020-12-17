from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

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


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password','first_name',)
        extra_kwargs = {
            'password':{'write_only': True},
        }
    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            password = validated_data['password'],
            first_name=validated_data['first_name'],
            )
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
