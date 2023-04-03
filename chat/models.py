from django.db import models

class Game(models.Model):
    player_one = models.CharField(max_length=255)
    player_two = models.CharField(max_length=255)
    current_player = models.CharField(max_length=255)
    board = models.CharField(max_length=9, default='         ')