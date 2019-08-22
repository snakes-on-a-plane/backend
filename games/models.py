from django.db import models

# Create your models here.
class Game(models.Model):
    flight = models.CharField(max_length=64)

    def __str__(self):
        return f'Flight: {self.flight}'

