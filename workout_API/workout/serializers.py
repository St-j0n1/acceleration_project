from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from .models import Items, Exercises, Muscles


class MusclesRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Muscles
        fields = ['id', 'name']


class ItemsRegisterSerializer(serializers.ModelSerializer):
    can_be_used_for = serializers.PrimaryKeyRelatedField(queryset=Muscles.objects.all(), many=True)

    class Meta:
        model = Items
        fields = ['name', 'can_be_used_for']


class ExercisesRegisterSerializer(serializers.ModelSerializer):
    target_muscle = serializers.PrimaryKeyRelatedField(queryset=Muscles.objects.all(), many=True)

    class Meta:
        model = Exercises
        fields = ['name', 'level', 'description', 'instruction', 'target_muscle', 'items',
                  'number_of_sets', 'number_of_reps', 'avg_time']
