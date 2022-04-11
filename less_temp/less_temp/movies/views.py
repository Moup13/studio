from django.shortcuts import render, get_object_or_404
from .models import Movie, Genre


# Create your views here.
def movie_list(request, genre_slug=None):
    genre = None
    genres = Genre.objects.all()
    movies = Movie.objects.filter()
    if genre_slug:
        genre =get_object_or_404(Genre,slug=genre_slug)
        movies =movies.filter(genres=genre)

    context={'genre':genre, 'genres':genres,'movies':movies}
    return render(request,'movies_list.html',context)


def movie_detail(request,id,slug):
    movie=get_object_or_404(Movie,id=id,slug=slug)
    context={'art':art}
    return render(request, 'movie_detail.html',context)