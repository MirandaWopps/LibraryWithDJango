from django.urls.conf import path
from . import views
from .views import livro

app_name = "VersoLivro"

urlpatterns = [
    path('', views.home, name='home-livros'),
    path('<int:pk>', livro, name = 'livro'),
]