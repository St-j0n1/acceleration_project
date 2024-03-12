from .serializers import PlanCreateSerializer, WeigthTrackerSerializer
from .models import Plan, WeightTracker
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated


class CreatePlanView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PlanCreateSerializer
    queryset = Plan.objects.all()


class UserWorkoutsListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PlanCreateSerializer

    def get_queryset(self):
        user = self.request.user
        return Plan.objects.filter(owner=user)


class UserWorkoutsDetailView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WeigthTrackerSerializer
    queryset = WeightTracker


class UserWeightsListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WeigthTrackerSerializer

    def get_queryset(self):
        user = self.request.user
        return WeightTracker.objects.filter(user=user).order_by('-id')