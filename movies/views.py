from django.shortcuts import render, redirect
from .models import Movies
from .forms import MovieForm


# Create your views here.
def index(request):
    all_movies = Movies.objects.all()
    return render(request, 'movies/movie_index.html', context={'movies': all_movies})


def movie_create(request):
    form = MovieForm()

    if request.method == 'POST':
        form = MovieForm(data=request.POST, files=request.FILES)
        if request.method == 'POST':
            if form.is_valid():


                form.save()
                return redirect('movie-index')

    return render(request, 'movies/create_form.html', context={'form': form})


def movie_update(request, pk):
    movie = Movies.objects.get(id=pk)
    form = MovieForm(instance=movie)

    if request.method == 'POST':
        form = MovieForm(data=request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie-detail', pk=movie.id)

    return render(request, 'movies/movie_update.html', context={'form': form, 'movie': movie})


def movie_delete(request, pk):
    Movies.objects.get(id=pk).delete()
    return redirect('movie-index')


def movie_detail(request, pk):
    movie = Movies.objects.get(pk=pk)
    return render(request, 'movies/movie_detail.html', context={'movie': movie})
