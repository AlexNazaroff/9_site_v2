from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, '<h4>Site Test SeleniumWebdriver</h4>'),

def about(request):
    return render('<h4>About SeleniumWebdriver</h4>'),


# python manage.py runserver
