from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserRegisterSerializer
from rest_framework import status
from rest_framework import generics


class RegistrationView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()

