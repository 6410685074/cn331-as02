from django.urls import path,include,re_path
from django.contrib import admin
from myapp import views

urlpatterns=[
    path('',view=views.index),
    path('about',views.about),
    path('login',views.user_login,name='login'),
    path('logout',views.user_logout,name='logout'),
    path('regis',views.regis,name='regis'),
    path('account_reg',views.account_reg,name='account_reg'),
]