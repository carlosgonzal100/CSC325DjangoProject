from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello, World! This the home page of my django application</h1>")

def about(request):
    return HttpResponse("<h1>About Page </h1><p> This is Project is about Django</p>")
