from rest_framework import serializers
from games.models import Game, Cell

class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = ('id', 'flight')

class CellSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cell
        fields = ('id','kind','movement_cost','x_pos','y_pos')
        