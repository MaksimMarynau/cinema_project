from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from django.db import models


from .models import Movie, Ticket
from . import serializers
from .service import get_client_ip


class MovieListView(APIView):
    """Information about list of movies"""

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        movies = Movie.objects.all()
        serializer = serializers.MovieListSerializer(movies, many=True)
        return Response(serializer.data)


class MovieDetailView(APIView):
    """Description movie"""

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        movie = Movie.objects.get(id=pk)
        serializer = serializers.MovieDetailSerializer(movie)
        return Response(serializer.data)

class TicketView(APIView):
    """Information about tickets"""

    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,pk):
        ticket = Ticket.objects.filter(movie=pk, ip=get_client_ip(request))
        serializer = serializers.TicketSerializer(ticket, many=True)
        return Response(serializer.data)

class BuyTicketView(APIView):
    """Buy a ticket"""

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = serializers.BuyTicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(ip=get_client_ip(request))
            return Response(status=201)
        else:
            return Response(status=400)
