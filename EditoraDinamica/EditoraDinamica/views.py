from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.
#def home(request):
  # processamento abaixo antes de mostrar a home page
 

# Create your views here.
def home(request):
# processamento antes de mostrar a home page
    return render(request, 'EditoraDinamica/index.html')