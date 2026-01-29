from django.urls import path
from . import views

urlpatterns = [
    path('hello',views.hello_world,name='hello_world'),
    path('',views.app_view,name='apps'),
    path('person/<int:person_id>',views.person_details,name='person_details'),
    path('name/<str:name>',views.username,name='username'),
    path('query',views.user_query,name='userquery'),
    path('redirect',views.my_redirect,name='redirect'),
    path('post',views.my_post,name='my_post'),
    path('submit',views.my_submit,name='my_submit'),
    path('submit_myform',views.form_submit,name='form_submit'),
    path('templating',views.template_view,name='templating'),
    path('delete_app/<int:app_id>',views.delete_app,name='delete_app'),
    path('toggle_app/<int:app_id>',views.toggle_is_verified,name='update_app'),
]