from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings


# Create your models here.

class Movies(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(verbose_name='Movie Description')
    likes = models.IntegerField(default=0)
    watch_count = models.IntegerField(default=0)
    rate = models.PositiveIntegerField(default=0)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    poster = models.ImageField(upload_to='movie/images')
    video = models.FileField(upload_to='movie/videos')
    actors = models.ManyToManyField('Cast')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'movie'


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(verbose_name='Category Description')
    movies_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Cast(models.Model):
    the_hero_name = models.CharField(max_length=255)
    director_name = models.CharField(max_length=255)
    cameraman_name = models.CharField(max_length=255)
    id_number = models.OneToOneField("IdNumber", on_delete=models.CASCADE)

    def __str__(self):
        return self.the_hero_name


class review(models.Model):
    comment = models.TextField()
    movie = models.ForeignKey("Movies", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return '{}_review'.format(self.movie.name)


class IdNumber(models.Model):
    number = models.CharField(max_length=150, default=0)

    def __str__(self):
        return self.number
