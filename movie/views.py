from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

# Create your views here.
def movie_show(request):
    movies = Movie.objects.all()
    return render(request, 'movie/movie_show.html', {'movies': movies})

def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    return render(request, 'movie/movie_detail.html', {'movie': movie})