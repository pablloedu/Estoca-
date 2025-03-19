from django.db import models

class Produto(models.Model):
    categoria = models.CharField(max_length=100)
    nome = models.CharField(max_length=200)
    quantidade_estoque = models.PositiveIntegerField()
    quantidade_pacote = models.PositiveIntegerField()
    preco_compra = models.DecimalField(max_digits=10, decimal_places=3)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=3)
    margem_lucro = models.FloatField()

    def __str__(self):
        return self.nome