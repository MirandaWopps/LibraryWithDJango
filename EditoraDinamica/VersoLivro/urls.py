from django.urls.conf import path
from VersoLivro import views

app_name = "VersoLivro"

urlpatterns = [
    path('', views.home, name='home-livros'),
]