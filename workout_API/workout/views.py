from django.shortcuts import render
from .models import Muscles, Items, Exercises
from .serializers import MusclesRegisterSerializer, ItemsRegisterSerializer, ExercisesRegisterSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny


class CreateMuscleView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = MusclesRegisterSerializer
    queryset = Muscles.objects.all()


class ListMusclesView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = MusclesRegisterSerializer
    queryset = Muscles.objects.all()


class CreateItemView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ItemsRegisterSerializer
    queryset = Items.objects.all()


class ListItemsView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ItemsRegisterSerializer
    queryset = Items.objects.all()


class CreateExerciseView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ExercisesRegisterSerializer
    queryset = Exercises.objects.all()


class ListExercisesView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ExercisesRegisterSerializer
    queryset = Exercises.objects.all()
