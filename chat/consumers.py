import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Game

class TicTacToeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.game_id = self.scope['url_route']['kwargs']['game_id']
        self.game_group_name = 'game_%s' % self.game_id

        # Join game group
        await self.channel_layer.group_add(
            self.game_group_name,
            self.channel_name
        )

        await self.accept()

        # Load game state from database
        self.game = await self.get_game(self.game_id)

    async def disconnect(self, close_code):
        # Leave game group
        await self.channel_layer.group_discard(
            self.game_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        action = text_data_json['action']
        data = text_data_json['data']

        if action == 'move':
            # Make move and save game state
            self.game.board = data['board']
            self.game.current_player = data['current_player']
            await self.save_game(self.game)

        # Send game state to all players
        await self.channel_layer.group_send(
            self.game_group_name,
            {
                'type': 'game_update',
                'data': {
                    'board': self.game.board,
                    'current_player': self.game.current_player,
                }
            }
        )

    async def game_update(self, event):
        data = event['data']

        # Send game state to WebSocket
        await self.send(text_data=json.dumps({
            'action': 'update',
            'data': data
        }))

    @staticmethod
    async def get_game(game_id):
        try:
            game = await Game.objects.get(id=game_id)
        except Game.DoesNotExist:
            return None
        return game

    @staticmethod
    async def save_game(game):
        await game.save()
