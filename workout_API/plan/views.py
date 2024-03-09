from .serializers import PlanSerializer
from .models import Plan
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny


class CreatePlanView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = PlanSerializer
    queryset = Plan.objects.all()
