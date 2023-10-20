from django.urls import path
from .views import *

urlpatterns = [
  path('', ListTodo.as_view()),
  path('update/<int:pk>/', UpdateTodo.as_view()),
  path('create', CreateTodo.as_view()),
  path('delete/<int:pk>/', DeleteTodo.as_view()),
]