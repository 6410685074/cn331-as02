from django.urls import path,include,re_path
from django.contrib import admin
from courses import views

urlpatterns=[
    path('course_info',view=views.course_info,name='course_info'),
    ]