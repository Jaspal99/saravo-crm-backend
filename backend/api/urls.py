from django.urls import path
from . import views

urlpatterns = [
    path('todo/',views.TodoListCreateView.as_view()),
    path('todo/<int:pk>',views.TodoRetrieveUpdateDestroyView.as_view())
]