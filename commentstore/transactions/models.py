from django.db import models
from django.contrib.auth.models import User

class Points(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=100)

    def __str__(self):
        return f'User: {self.name.username}, Points: {self.points}'

class PointsTransfer(models.Model):
    enter_your_username = models.CharField(max_length=50)
    enter_destination_username = models.CharField(max_length=50)
    enter_points_to_transfer = models.IntegerField()

    def __str__(self):
        return f'From: {self.enter_your_username}, To: {self.enter_destination_username}, Points: {self.enter_points_to_transfer}'
