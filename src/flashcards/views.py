from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from flashcards.models import MovieSet


@login_required
def load_decks(request):
    movie_sets = request.user.movieset_set.all().order_by('-date_added')
    context = {'movie_sets': movie_sets}
    return render(request, 'flashcards/decks.html', context)


@login_required
def show_flashcards(request, set_id):
    movie_set = get_object_or_404(MovieSet, id=set_id)
    # print(movie_set.flash)
    context = {'set': movie_set}
    return render(request, 'flashcards/set.html', context)
