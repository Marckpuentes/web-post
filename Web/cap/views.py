from django.shortcuts import render
from .models import Cap
from post.models import CreatePost
from django.views.generic.list import ListView

class ListCap(ListView):
    model = Cap



