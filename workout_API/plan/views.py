from urllib import request

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PlanSerializer
from .models import Plan
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated


class CreatePlanView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PlanSerializer
    queryset = Plan.objects.all()


class UserWorkoutListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PlanSerializer

    def get_queryset(self):
        user = self.request.user
        return Plan.objects.filter(owner=user)
