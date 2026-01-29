from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotAllowed
from .forms import PersonForm ,AppForm
from .models import App,Person

def hello_world(request):
    return HttpResponse('Hello World')

# def app(request):
#     return render(request,'app/app.html')

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

def template_view(request):
    context = {
        "name" : "mike",
        "age": 30,
        "skills": ["Python","Laravel","Django","React","K8s"]
    }

    return render(request,'app/mytempate.html',context)

def app_view(request):
    if request.method == 'POST':
        form = AppForm(request.POST)

        if form.is_valid():
            app = form.save()
            return HttpResponse('App successfully created!')
    else:
        form = AppForm()

        apps = App.objects.all()

        return render(request,'app/app.html', {'form':form,'apps': apps})

def person_details(request, person_id):
    person = Person.objects.filter(id=person_id).first()

    return render('app/person_details.html',{'person': person})

def delete_app(request,app_id):
    app = App.objects.filter(id=app_id).first()
    app.delete()

    return HttpResponse('App successfully deleted!')

def toggle_is_verified(request, app_id):
    app = App.objects.filter(id=app_id).first()
    app.is_verified = not app.is_verified
    app.save()

    return HttpResponse('App successfully updated!')

# Create your views here.
