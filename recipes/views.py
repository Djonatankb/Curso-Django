from django.shortcuts import render
from django.http import HttpResponse


def sobre(request):
    return HttpResponse('SOBRE')


def home(request):
    return render(request, 'recipes/home.html')


def contato(request):
    return HttpResponse('CONTATO')

# Create your views here.
