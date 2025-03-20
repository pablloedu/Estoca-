from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Produto
from .forms import ProdutoForm
# Create your views here.

def listar_produtos(request):
    query = request.GET.get('q')  # Obtém o termo de busca
    
    if query:
        produtos = Produto.objects.filter(nome__icontains=query)
    else:
        produtos = Produto.objects.all()

    # Cálculo do preço unitário e preço final para cada produto
    for produto in produtos:
        # Cálculo do preço unitário
        preco_unitario = produto.preco_compra / produto.quantidade_pacote if produto.quantidade_pacote != 0 else 0
        
        # Cálculo do preço final com margem de lucro
        preco_final = preco_unitario * (1 + produto.margem_lucro / 100)
        
        # Adicionar os valores ao produto
        produto.preco_unitario = round(preco_unitario, 2)
        produto.preco_final = round(preco_final, 2)

    # Paginação: 10 produtos por página
    paginator = Paginator(produtos, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'estoque/listar_produtos.html', {'page_obj': page_obj, 'query': query})

def cadastrar_produto(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'estoque/cadastrar_produto.html', {'form': form})

def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm(instance=produto)

    return render(request, 'estoque/editar_produto.html', {'form': form, 'produto': produto})

def excluir_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == "POST":
        produto.delete()
        return redirect('listar_produtos')

    return render(request, 'estoque/excluir_produto.html', {'produto': produto})

