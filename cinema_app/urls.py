from django.contrib import admin
from django.urls import path
from django.urls import include

from . import views

urlpatterns = [
    path("movie/", views.MovieListView.as_view()),
    path("movie_detail/<int:pk>/", views.MovieDetailView.as_view()),
    path("ticket/<int:pk>/", views.TicketView.as_view()),
]
