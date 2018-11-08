from django.urls import path
from . import views

urlpatterns = [
        path('', views.TodoListView.as_view(), name = 'todo_list'),
        path('detail/<int:id>/', views.TodoDetailView.as_view(), name = 'todo_detail'),
        path('create/', views.TodoCreateView.as_view(), name = 'todo_form'),
        path('update/<int:id>/', views.TodoUpdateView.as_view(), name = 'todo_update'),
        path('detele/<int:id>/', views.TodoDeleteView.as_view(), name = 'todo_delete'),
        ]

