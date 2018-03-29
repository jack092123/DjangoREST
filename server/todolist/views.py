from django.shortcuts import render
import os

# Create your views here.
def hello_django(request):
    return render(request, 'hello_django.html', {
        'data' : 'Hello World!! Hello Django~~'
    })

def todolist_view(request):
    return render(request, 'todolist.html', {})

def edit_view(request, todo_id):
    return render(request, 'edit.html', {})
