from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse('Hello World')

def app(request):
    return render(request,'app/app.html')

# Create your views here.
