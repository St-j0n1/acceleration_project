from django.urls import path
from .views import CreatePlanView, UserWorkoutsListView, UserWeightsListView, UserWorkoutsDetailView

urlpatterns = [
    path('create/', CreatePlanView.as_view(), name='create_plan'),
    path('list/', UserWorkoutsListView.as_view(), name='user-plan'),

    path('weight/', UserWorkoutsDetailView.as_view(), name='weight'),
    path('weight/history/', UserWeightsListView.as_view(), name='history')
]