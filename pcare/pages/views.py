from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request,'pages/home.html')
def index(request):
    return render(request,'pages/about.html')
def contact(request):
    return render(request,'pages/contact.html')

def health(request):
    return render(request,'careyourself/healthy_diet.html')
def awareness(request):
    return render(request,'careyourself/awareness.html')
def exercises(request):
    return render(request,'careyourself/exercises.html')
def medicine(request):
    return render(request,'careyourself/medicine.html')
def mental(request):
    return render(request,'careyourself/mental.html')