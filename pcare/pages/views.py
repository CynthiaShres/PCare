from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1> This is my home page </h1>')

def index(request):
    return render(request,'pages/about.html')

def index(request):
    return render(request,'careyourself/healthy_diet.html')