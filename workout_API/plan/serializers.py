from rest_framework import serializers
from .models import Plan, WeightTracker
from workout.models import Exercises


class ExercisesSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='Exercise_Name', read_only=True)
    model = Exercises
    fields = ('id', 'name', 'number_of_sets', 'number_of_reps')


class PlanCreateSerializer(serializers.ModelSerializer):
    exercises = serializers.PrimaryKeyRelatedField(queryset=Exercises.objects.all(), many=True)

    class Meta:
        model = Plan
        fields = ['id', 'owner', 'title', 'exercises', 'private']
        read_only_fields = ['owner']

    def create(self, validated_data):
        user = self.context.get('request').user
        exercises_data = validated_data.pop('exercises')
        new_plan = Plan.objects.create(owner=user, **validated_data)
        new_plan.exercises.set(exercises_data)
        return new_plan


class WeigthTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeightTracker
        fields = ['id', 'user', 'date', 'weight']
        read_only_fields = ['user']

    def create(self, validated_data):
        user = self.context.get('request').user
        new_weight = WeightTracker(user=user, **validated_data)
        new_weight.save()

        return new_weight
