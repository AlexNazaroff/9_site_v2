from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, '<h4>Site Test SeleniumWebdriver</h4>'),

def index(request):
    return HttpResponse('<h4>Site Test SeleniumWebdriver</h4>'),


# python manage.py runserver
