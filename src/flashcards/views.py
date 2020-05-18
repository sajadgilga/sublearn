import redis
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from EnglishLearning import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import MovieSet
from .serializers import MovieSerializer

redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                  port=settings.REDIS_PORT, db=0)

@login_required
@api_view(['GET'])
def load_decks(request):
    movie_sets = request.user.movieset_set.all().order_by('-date_added')
    movies = MovieSerializer(movie_sets, many=True)
    return Response(movies)
    # context = {'movie_sets': movie_sets, 'title': 'Flashcard Decks'}
    # return render(request, 'flashcards/decks.html', context)


@login_required
@api_view(['GET'])
def show_flashcards(request, set_id):
    movie_set = get_object_or_404(MovieSet, id=set_id)
    movies = MovieSerializer(movie_set)
    return Response(movies)

    # context = {'set': movie_set, 'title': movie_set.movie_name + " Flashcards"}
    # return render(request, 'flashcards/set.html', context)
