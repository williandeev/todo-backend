from django.shortcuts import render
from rest_framework import generics 
from .serializers import *
from .models import *

#CRUD

class ListTodo(generics.ListCreateAPIView):     #Read
  queryset = ToDo.objects.all()
  serializer_class = ToDoSerializer

class DetailTodo(generics.RetrieveUpdateDestroyAPIView):    #Update
  queryset = ToDo.objects.all()
  serializer_class = ToDoSerializer

class UpdateTodo(generics.UpdateAPIView):
  queryset = ToDo.objects.all()
  serializer_class = ToDoSerializer

class CreateTodo(generics.CreateAPIView):      #Create
  queryset = ToDo.objects.all()
  serializer_class = ToDoSerializer

class DeleteTodo(generics.DestroyAPIView):    #Delete
  queryset = ToDo.objects.all()
  serializer_class = ToDoSerializer