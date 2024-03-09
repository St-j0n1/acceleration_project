from django.urls import path
from .views import AddMuscleView, ListMusclesView, AddItemView, ListItemsView

urlpatterns = [
    path('muscle/', AddMuscleView.as_view(), name='add_muscle'),
    path('muscle/list/', ListMusclesView.as_view(), name='muscle-list'),

    path('item/', AddItemView.as_view(), name='add-item'),
    path('item/list/', ListItemsView.as_view(), name='item-list')
]
