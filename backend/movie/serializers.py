from django.db.models import Sum
from rest_framework import serializers

from .models import Movie, Actor, Genre, Review, Rating


class MovieSerializer(serializers.ModelSerializer):
    """
    Serializer for MovieViewSet
    """
    class Meta:
        model = Movie
        fields = '__all__'


class ActorSerializer(serializers.ModelSerializer):
    """
    Serializer for ActorViewSet
    """
    class Meta:
        model = Actor
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    """
    Serializer for GenreViewSet
    """
    class Meta:
        model = Genre
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializer for ReviewViewSet
    """
    class Meta:
        model = Review
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    """
    Serializer for ReviewViewSet
    """
    average_rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Rating
        fields = '__all__'

    def get_average_rating(self, obj):
        print(obj)
        return sum(obj.aggregate(Sum('ranking_score'))) / len(obj)
