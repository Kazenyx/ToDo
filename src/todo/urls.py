from django.urls import path
from . import views

urlpatterns = [
  path('', views.todo, name="todo"),
  path('delt/<str:pk>/', views.delt, name="delt"),
]
