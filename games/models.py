from django.db import models

# Create your models here.
class Game(models.Model):
    flight = models.CharField(max_length=64)

    def __str__(self):
        return f'Flight: {self.flight}'

class Cell(models.Model):
    kind = models.CharField(max_length=64, default='wall')

    movement_cost = models.IntegerField(default=0)
    x_pos = models.IntegerField()
    y_pos = models.IntegerField()

    def __str__(self):
        return f'{self.kind} : {self.x_pos},{self.y_pos}'


