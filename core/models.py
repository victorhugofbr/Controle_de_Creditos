from django.db import models

from django.db import models

class Empresa(models.Model):
    razao_social = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14)
    contato_telefone = models.CharField(max_length=15, default='(00) 0000-0000')

    def __str__(self):
        return self.razao_social

class PedidoRestituicao(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='pedidos')
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_solicitacao = models.DateField(auto_now_add=True)
    pdf_file = models.FileField(upload_to='pedidos_pdfs/', null=True, blank=True)

    def __str__(self):
        return f"Pedido {self.id} da empresa {self.empresa.nome}"
