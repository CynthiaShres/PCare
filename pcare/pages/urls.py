from django.urls import path
from . import views

urlpatterns=[
    path('',views.index, name='index'),
    path('home',views.home, name='index'),
    path('about',views.index, name='index'),
    path('contact',views.contact, name='index'),

    path('healthy_diet',views.health, name='index'),
    path('awareness',views.awareness, name='index'),
    path('exercises',views.exercises, name='index'),
    path('medicine',views.medicine, name='index'),
    path('mental',views.mental, name='index'),
]