from django.urls import path
from .views import CreateMuscleView, ListMusclesView, CreateItemView, ListItemsView, CreateExerciseView,\
    ListExercisesView

urlpatterns = [
    path('muscle/', CreateMuscleView.as_view(), name='add_muscle'),
    path('muscle/list/', ListMusclesView.as_view(), name='muscle-list'),

    path('item/', CreateItemView.as_view(), name='add-item'),
    path('item/list/', ListItemsView.as_view(), name='item-list'),

    path('exercise/', CreateExerciseView.as_view(), name='create-exercise'),
    path('exercise/list/', ListExercisesView.as_view(), name='exercise-list')
]
