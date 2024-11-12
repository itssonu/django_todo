from django.urls import path
from . import views

urlpatterns = [
    path('create', views.createTodoView, name='createTodoUrl'),
    path('', views.todoList, name='todosListUrl'),
    path('up/<int:id>', views.updateTodo, name= 'updateTodoUrl'),
    path('del/<int:id>', views.deleteTodo, name= 'deleteTodoUrl'),
]
