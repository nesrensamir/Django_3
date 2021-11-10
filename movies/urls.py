from django.contrib import admin
from django.urls import path
from .views import index, movie_create, movie_delete, movie_update, movie_detail

urlpatterns = [
    path('index/', index, name='movie-index'),
    path('create/', movie_create, name='movie-create'),
    path('<int:pk>/delete/', movie_delete, name='movie-delete'),
    path('<int:pk>/update/', movie_update, name='movie-update'),
    path('<int:pk>/detail/', movie_detail, name='movie-detail'),

]
