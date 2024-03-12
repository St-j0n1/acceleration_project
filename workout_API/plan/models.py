from datetime import datetime
from django.db import models
from user.models import User
from workout.models import Items, Exercises, Muscles


class Achievements(models.Model):
    pass


class Plan(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    title = models.CharField(max_length=200, default='untitled')
    exercises = models.ManyToManyField(Exercises, related_name='exercises')
    private = models.BooleanField(default=False)


class WeightTracker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    date = models.DateField(auto_now_add=True)
    weight = models.FloatField()

    class Meta:
        ordering = ['date']
