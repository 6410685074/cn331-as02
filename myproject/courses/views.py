
from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import Student
from courses.models import Regis,Course
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
