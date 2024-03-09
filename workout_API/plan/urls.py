from django.urls import path
from .views import CreatePlanView

urlpatterns = [
    path('create/', CreatePlanView.as_view(), name='create_plan')
]