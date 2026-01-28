from django.urls import path
from . import views

urlpatterns = [
    path('hello',views.hello_world,name='hello_world'),
    path('app',views.app,name='my_app'),
    path('name/<str:name>',views.username,name='username'),
    path('query',views.user_query,name='userquery'),
    path('redirect',views.my_redirect,name='redirect'),
    path('post',views.my_post,name='my_post'),
    path('submit',views.my_submit,name='my_submit'),
    path('submit_myform',views.form_submit,name='form_submit'),
]