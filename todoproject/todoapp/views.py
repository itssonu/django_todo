from django.shortcuts import render
from .models import Todo

def helloWorld(request):
    template_name='hello_world.html'
    return render(request, template_name)

def index(request):
    templates = Todo.objects.all()
    template_name = 'index.html'
    context = {'templates': templates}
    return render(request, template_name, context)
