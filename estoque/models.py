from django.db import models

class Produto(models.Model):
    categoria = models.CharField(max_length=100)
    nome = models.CharField(max_length=255)
    quantidade_estoque = models.IntegerField()
    quantidade_pacote = models.IntegerField()
    preco_compra = models.DecimalField(max_digits=10, decimal_places=2)
    margem_lucro = models.DecimalField(max_digits=5, decimal_places=2)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def calcular_preco_venda(self):
        if self.preco_compra and self.margem_lucro:
            self.preco_venda = self.preco_compra * (1 + (self.margem_lucro / 100))

    def save(self, *args, **kwargs):
        self.calcular_preco_venda()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome