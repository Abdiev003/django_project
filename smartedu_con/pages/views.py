from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

def index(request):
    return HttpResponse('<h1>Index sayfasi</h1>')
