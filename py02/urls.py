from django.urls import path
from .views import CreateEventView

urlpatterns = [
    path('events/', CreateEventView.as_view(), name='create_event'),
]