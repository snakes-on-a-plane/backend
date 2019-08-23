from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import GameList, GameDetail, CellList, CellDetail

urlpatterns = [
    path('games/', GameList.as_view()),
    path('games/<int:pk>/', GameDetail.as_view()),
    path('cells/', CellList.as_view()),
    path('cells/<int:pk>/', CellDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)