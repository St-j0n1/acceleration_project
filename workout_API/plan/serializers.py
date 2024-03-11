from rest_framework import serializers
from .models import Plan
from workout.models import Exercises


class PlanSerializer(serializers.ModelSerializer):
    exercises = serializers.PrimaryKeyRelatedField(queryset=Exercises.objects.all(), many=True)

    class Meta:
        model = Plan
        fields = ['owner', 'title', 'exercises', 'private']
        read_only_fields = ['owner']

    def create(self, validated_data):
        user = self.context.get('request').user
        exercises_data = validated_data.pop('exercises')
        new_plan = Plan.objects.create(owner=user, **validated_data)
        new_plan.exercises.set(exercises_data)
        return new_plan
