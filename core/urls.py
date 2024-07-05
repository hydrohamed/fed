# myapp/urls.py
from django.urls import path
from .views import filtered_flood_events, index, detail

urlpatterns = [
    path('', index, name='index'),
    path('filtered-flood-events/', filtered_flood_events,
         name='filtered_flood_events'),
    path('event/<int:pk>/', detail, name='detail'),
]
