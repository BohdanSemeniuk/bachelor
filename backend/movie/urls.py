from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import MovieViewSet, ActorViewSet, GenreViewSet, ReviewViewSet, RatingViewSet

router = DefaultRouter()
router.register('movies', MovieViewSet)
router.register('actors', ActorViewSet)
router.register('genres', GenreViewSet)
router.register('reviews', ReviewViewSet)
router.register('ratings', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
