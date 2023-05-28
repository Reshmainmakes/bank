from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('',views.demo,name='demo'),
path('register.html/',views.register,name='register'),
path('login.html/',views.login,name='login'),
path('form.html/',views.form,name='form'),
path('button.html/',views.button,name='button'),

]