from django.urls import path
from .views import CreatePlanView, UserWorkoutListView

urlpatterns = [
    path('create/', CreatePlanView.as_view(), name='create_plan'),
    path('plan/', UserWorkoutListView.as_view(), name='')
]