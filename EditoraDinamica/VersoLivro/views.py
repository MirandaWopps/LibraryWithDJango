from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.

def home(request): 
    return render(request,'VersoLivro/index.html')