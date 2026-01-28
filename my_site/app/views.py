from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotAllowed
from .forms import PersonForm 

def hello_world(request):
    return HttpResponse('Hello World')

def app(request):
    return render(request,'app/app.html')

def username(request,name):
    return HttpResponse(f'Hello {name}!')

def user_query(request):
    return HttpResponse(f'Your query was {request.GET.get("q")}')

def my_redirect(request):
    return redirect('my_app')

def my_post(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            job = form.cleaned_data['job']
        return HttpResponse(f'You posted: {name}, {age}, {job}')
    else:
        return HttpResponseNotAllowed(['POST'])

def my_submit(request):
    return render(request,'app/submit.html')

def form_submit(request):
    form = PersonForm()
    return render(request,'app/form_submit.html',{'form':form})


# Create your views here.
