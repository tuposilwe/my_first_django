from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse('Hello World')

def app(request):
    return render(request,'app/app.html')

def username(request,name):
    return HttpResponse(f'Hello {name}!')

def user_query(request):
    return HttpResponse(f'Your query was {request.GET.get("q")}')

# Create your views here.
