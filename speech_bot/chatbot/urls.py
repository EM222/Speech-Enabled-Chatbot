from django.urls import path
from . import views

patterns = [
    path('api/messages', views.messages, name='messages'),
]