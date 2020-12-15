from rest_framework.response import Response
from rest_framework.views import APIView

from . import models
from . import serializers


class MovieListView(APIView):
    """Information about list of movies"""
    def get(self, request):
        movies = models.Movie.objects.all()
        serializer = serializers.MovieListSerializer(movies, many=True)
        return Response(serializer.data)


class MovieDetailView(APIView):
    """Description movie"""
    def get(self, request, pk):
        movie = models.Movie.objects.get(id=pk)
        serializer = serializers.MovieDetailSerializer(movie)
        return Response(serializer.data)

class TicketView(APIView):
    """Information about ticket"""
    def get(self,request,pk):
        ticket = models.Ticket.objects.get(id=pk)
        serializer = serializers.TicketSerializer(ticket)
        return Response(serializer.data)
