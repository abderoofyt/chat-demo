from django.urls import path
from . import views

urlpatterns = [
    path('', views.new_game, name='new_game'),
    path('tictactoe/<int:game_id>/', views.game_detail, name='game'),
]