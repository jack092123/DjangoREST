from django.shortcuts import render

# Create your views here.
def hello_django(request):
    return render(request, 'hello_django.html', {
        'data' : 'Hello World!! Hello Django~~'
    })
