from django.shortcuts import render

from rest_api.models import Todo
from rest_api.serializers import TodoSerializer

from rest_framework import viewsets

# Create your views here.
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


def hello_django(request):
    return render(request, 'hello_django.html', {
        'data' : 'Hello World!! Hello Django~~'
    })
