from django.shortcuts import render
from .models import Muscles, Items
from .serializers import MusclesRegisterSerializer, ItemsRegisterSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny


class AddMuscleView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = MusclesRegisterSerializer
    queryset = Muscles.objects.all()


class ListMusclesView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = MusclesRegisterSerializer
    queryset = Muscles.objects.all()


class AddItemView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ItemsRegisterSerializer
    queryset = Items.objects.all()


class ListItemsView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ItemsRegisterSerializer
    queryset = Items.objects.all()
