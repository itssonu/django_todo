from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

def helloWorld(request):
    template_name='hello_world.html'
    return render(request, template_name)

def createTodoView(request):
    form = TodoForm
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    template_name = "todo.html"
    context = {"form": form}
    return render(request, template_name, context)

def showTodoView(request):
    obj = Todo.objects.all()
    template_name = "show.html"
    context = {"obj": obj}
    return render(request, template_name, context)

def updateTodoView(request, f_id):
    obj = Todo.objects.get(id=f_id)
    form = TodoForm(instance=obj)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    template_name = "todo.html"
    context = {"form": form}
    return render(request, template_name, context)

def deleteTodoView(request, f_id):
    obj = Todo.objects.get(id = f_id)
    if request.method == "POST":
        obj.delete()
        return redirect("show_url")
    template_name = "confirmation.html"
    context = {"obj": obj}
    return render(request, template_name, context)