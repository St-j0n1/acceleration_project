from rest_framework import serializers
from .models import Plan
from workout.models import Exercises


class PlanSerializer(serializers.ModelSerializer):
    exercises = serializers.PrimaryKeyRelatedField(queryset=Exercises.objects.all(), many=True)

    class Meta:
        model = Plan
        fields = ['owner', 'title', 'exercises', 'private']
