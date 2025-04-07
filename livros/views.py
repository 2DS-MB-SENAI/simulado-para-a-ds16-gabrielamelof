from django.shortcuts import render
from .models import Livro

# Create your views here.
def lista_livros(request):
    livros = Livro.objects.all()
    return render(request, 'livros.html', {'livros': livros})