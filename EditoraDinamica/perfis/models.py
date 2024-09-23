from django.db import models

# Create your models here.
class Pessoa(models.Model):
    TIPO_USUARIO = {
        "E": "EDITOR",
        "R": "REVISOR",
        "L": "LEITOR",
    } 

    id = models.AutoField(primary_key=True)
    
    nome = models.CharField(max_length=100, help_text='nome')

    email = models.EmailField(help_text='Informe o email', max_length=70)

    tpUser = models.CharField(max_length=1, choices=TIPO_USUARIO)
    


    
