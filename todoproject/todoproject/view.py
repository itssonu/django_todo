from django.shortcuts import render

def helloWorld(request):
    return render(request, template_name='hello_world.html')