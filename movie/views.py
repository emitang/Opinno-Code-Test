from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

# Create your views here.
def movie_show(request):
    movie = Movie.objects.order_by('rating')
    return render(request, 'movie/movie_show.html', {'movie': movie})