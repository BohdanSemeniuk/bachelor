from rest_framework import viewsets, permissions

from .models import Movie, Actor, Genre, Review, Rating
from .permissions import IsStaffOrSafeMethodsPermission, IsOwnerOrReadAndCreateOnly
from .serializers import MovieSerializer, ActorSerializer, GenreSerializer, ReviewSerializer, RatingSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """
    ViewSet to work with movies
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsStaffOrSafeMethodsPermission, permissions.IsAuthenticatedOrReadOnly]


class ActorViewSet(viewsets.ModelViewSet):
    """
    ViewSet to work with actors and directors
    """
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [IsStaffOrSafeMethodsPermission, permissions.IsAuthenticatedOrReadOnly]


class GenreViewSet(viewsets.ModelViewSet):
    """
    ViewSet to work with genres
    """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsStaffOrSafeMethodsPermission, permissions.IsAuthenticatedOrReadOnly]


class ReviewViewSet(viewsets.ModelViewSet):
    """
    ViewSet to work with review
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsOwnerOrReadAndCreateOnly, permissions.IsAuthenticatedOrReadOnly]


class RatingViewSet(viewsets.ModelViewSet):
    """
    ViewSet to work with rating
    """
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsOwnerOrReadAndCreateOnly, permissions.IsAuthenticatedOrReadOnly]
