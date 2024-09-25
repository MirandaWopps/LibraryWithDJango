from django.shortcuts import render
from django.views.generic.base import View
from . models import Livro

# Create your views here.

def home(request):
    livros = Livro.objects.all()
    return render(request,'VersoLivro/index.html')

def livro(request, pk):
    return render(request,'VersoLivro/index.html')