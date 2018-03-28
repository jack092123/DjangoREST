from django.shortcuts import render
import requests
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def hello_django(request):
    return render(request, 'hello_django.html', {
        'data' : 'Hello World!! Hello Django~~'
    })

def todolist_view(request):
    todolist_data = requests.get('http://127.0.0.1:8000/api/Todo/')
    logger.error(todolist_data.json())
    return render(request, 'todolist.html', {
        'data' : todolist_data.json()
    })