from django.shortcuts import render
from . models import Content

from django.views.generic import ListView
# Create your views here.

def homeView(request):
    context = {}
    return render(request, 'blog/index.html', context)
    