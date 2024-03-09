from django.db import models
from user.models import User
from workout.models import Items, Exercises, Muscles


class Plan(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    title = models.CharField(max_length=200, default='untitled')
    exercises = models.ManyToManyField(Exercises, related_name='exercises')
    private = models.BooleanField(default=False)


