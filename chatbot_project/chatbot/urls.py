from django.urls import path
from . import views

urlpatterns = [
    path('Chatbot/', views.chatbot, name='chatbot'),
]