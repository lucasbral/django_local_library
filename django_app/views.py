

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
   
    # Retorna uma resposta renderizada para enviar ao cliente.
    # Fazemos uso da função de atalho para facilitar tudo.
    # Note que o primeiro parâmetro é o template que desejamos usar.
    return render(request, 'django/index.html')