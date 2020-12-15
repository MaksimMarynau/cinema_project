from django.contrib import admin
from django import forms
# Register your models here.


from . import models


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
	list_display = ('title','description','price','rating')
	list_filter = ('title',)
	search_fields = ('title',)
	save_on_top = True
	save_as = True


@admin.register(models.Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('amount','movie')
