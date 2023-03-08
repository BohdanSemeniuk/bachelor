from django.contrib.auth.models import User
from django.db import models
from datetime import date


class Actor(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to="actors/")
    url = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Актори та режисери"
        verbose_name_plural = "Актори та режисери"
        ordering = ['name']


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанри"


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    poster = models.ImageField(upload_to="movies/")
    year = models.PositiveSmallIntegerField(default=date.today().year)
    country = models.CharField(max_length=50)
    directors = models.ManyToManyField(Actor, related_name="film_director")
    actors = models.ManyToManyField(Actor, related_name="film_actor")
    genre = models.ManyToManyField(Genre)
    world_premiere = models.DateField(default=date.today)
    budget = models.PositiveIntegerField(default=0)
    fees_in_world = models.PositiveIntegerField(default=0)
    url = models.SlugField(max_length=255, unique=True)
    draft = models.BooleanField(default=False)
    youtube_trailer_url = models.SlugField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фільм"
        verbose_name_plural = "Фільми"
        ordering = ['title']


class Review(models.Model):
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=10000)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.movie}"

    class Meta:
        verbose_name = "Відгук"
        verbose_name_plural = "Відгуки"


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    ranking_score = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.ranking_score

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"
