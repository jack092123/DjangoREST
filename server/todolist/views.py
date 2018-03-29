from django.shortcuts import render
from . import services
import os

port = os.environ.get('DJANGO_PORT')
if port == None:
    port = r'8000'

# Create your views here.
def hello_django(request):
    return render(request, 'hello_django.html', {
        'data' : 'Hello World!! Hello Django~~'
    })

def todolist_view(request):
    return render(request, 'todolist.html', {
        'data' : services.get_todolist(port).json()
    })

def edit_view(request, todo_id):
    return render(request, 'edit.html', {
        'data' : services.get_todo(port, todo_id).json()
    })