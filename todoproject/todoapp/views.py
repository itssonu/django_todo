from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

def createTodoView(request):
    form = TodoForm
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todosListUrl")
    template_name = "create.html"
    context = {"form": form}
    return render(request, template_name, context)

def todoList(request):
    data = Todo.objects.all()
    template_name = "index.html"
    context = {"data": data}
    return render(request, template_name, context)

def updateTodo(request, id):
    obj = Todo.objects.get(id=id)
    form = TodoForm(instance=obj)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("todosListUrl")
    template_name = "create.html"
    context = {"form": form}
    return render(request, template_name, context)

def deleteTodo(request, id):
    obj = Todo.objects.get(id=id)
    if request.method == "POST":
        obj.delete()
        return redirect("todosListUrl")
    template_name = "confirmation.html"
    context = {"obj": obj}
    return render(request, template_name, context)