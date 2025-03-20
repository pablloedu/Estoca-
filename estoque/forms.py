from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['categoria', 'nome', 'quantidade_estoque', 'quantidade_pacote', 'preco_compra', 'margem_lucro']