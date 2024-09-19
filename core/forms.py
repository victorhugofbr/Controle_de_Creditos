from django import forms
from .models import Empresa, PedidoRestituicao

from django import forms
from .models import Empresa

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['razao_social', 'cnpj', 'contato_telefone']  # Atualize os campos
        labels = {
            'razao_social': 'Razão Social',
            'contato_telefone': 'Contato Telefone',
            'cnpj':'CNPJ'
        }
        widgets = {
            'razao_social': forms.TextInput(attrs={'class': 'form-control'}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control'}),
            'contato_telefone': forms.TextInput(attrs={'class': 'form-control'}),  # Novo campo
        }

class PedidoRestituicaoForm(forms.ModelForm):
    class Meta:
        model = PedidoRestituicao
        fields = ['descricao', 'valor', 'pdf_file']
