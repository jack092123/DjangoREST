from django.shortcuts import render
import requests
import os

# Create your views here.
def hello_django(request):
    return render(request, 'hello_django.html', {
        'data' : 'Hello World!! Hello Django~~'
    })

def todolist_view(request):
    port = os.environ.get('DJANGO_PORT')
    if port == None:
        port = r'8000'
    
    url = 'http://127.0.0.1:' + port + '/api/Todo/'
    todolist_data = requests.get(url)
    return render(request, 'todolist.html', {
        'data' : todolist_data.json()
    })