from django.db import models

# Create your models here.

class Movie(models.Model):
    """Information about movie"""
    title = models.CharField('Title',max_length = 100)
    description = models.TextField('Description')
    price = models.PositiveSmallIntegerField(default=0)
    rating = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Movie'
        verbose_name_plural='Movies'

class Ticket(models.Model):
    """Information about ticket"""
    amount = models.PositiveSmallIntegerField(default=0)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.amount}'

    class Meta:
        verbose_name='Ticket'
        verbose_name_plural='Tickets'
