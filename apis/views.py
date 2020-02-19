from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework import viewsets

from todos import models
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer