from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .form import NewGameForm
from .models import Game

def new_game(request):
    if request.method == 'POST':
        form = NewGameForm(request.POST)
        if form.is_valid():
            game = form.save()
            return HttpResponseRedirect('/tictactoe/%d/' % game.id)
    else:
        form = NewGameForm()
    return render(request, 'chat/new_game.html', {'form': form})

def game_detail(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    return render(request, 'chat/game.html', {'game': game})
