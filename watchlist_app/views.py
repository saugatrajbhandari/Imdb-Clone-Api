from django.shortcuts import render
from .models import Movie
from django.http import JsonResponse

def movie_list(request):
    movie = Movie.objects.values()
    return JsonResponse({'movies': list(movie)})