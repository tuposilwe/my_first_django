from django.urls import path
from . import views

urlpatterns = [
    path('hello',views.hello_world,name='hello world'),
    path('app',views.app,name='my app'),
]