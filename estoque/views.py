from django.shortcuts import render
from .models import Produto
# Create your views here.

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render (request, 'estoque/listar_produtos.html', {'produtos': produtos}) 