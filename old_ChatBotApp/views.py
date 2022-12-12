from django.shortcuts import render
from . import forms
from django.views.generic.list import ListView
from .models import ChatBotModel

# Create your views here.

class ChatBot(ListView):
    template_name = 'rooms/room_kuramochi.html'
    model = ChatBotModel
