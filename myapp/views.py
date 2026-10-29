from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

def home(request):
    return HttpResponse("<h1>Hello, World! This the home page of my django application</h1>")

def about(request):
    return HttpResponse("<h1>About Page </h1><p> This is Project is about Django</p>")

@api_view(['GET'])
def hello_api(request):
    return Response({
        "message": "Hello from the CSC325 Django API",
        "course": "CSC325",
        "student": "Carlos Gonzalez",
    })
