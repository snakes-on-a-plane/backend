from rest_framework import generics
from games.models import Game, Cell
from .serializers import GameSerializer, CellSerializer

class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class CellList(generics.ListCreateAPIView):
    queryset = Cell.objects.all()
    serializer_class = CellSerializer


class CellDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cell.objects.all()
    serializer_class = CellSerializer