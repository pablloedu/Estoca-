from django.urls import path
from .views import listar_produtos, cadastrar_produto

urlpatterns = [
    path('', listar_produtos, name='listar_produtos'),
    path('cadastrar/', cadastrar_produto, name='cadastrar_produto'),
]