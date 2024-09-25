from django.shortcuts import render
#from django.http import HttpResponse

from VersoLivro.models import Livro


# Create your views here.
def home(request):
    livros = Livro.objects.all()

    capa = livros.values_list('capa')
    livros_dict = {'capa': capa}
    
    return render(request, 'EditoraDinamica/index.html', livros_dict)

