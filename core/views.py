from django.shortcuts import render, get_object_or_404, redirect
from .models import Empresa, PedidoRestituicao
from .forms import EmpresaForm, PedidoRestituicaoForm

def listar_empresas(request):
    form = EmpresaForm()
    return render(request, 'core/listar_empresas.html', {'form': form})

def cadastrar_empresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            cad = form.save(commit=False)

            print(f"Razão Social: {cad.razao_social}")
            form.save()
            return redirect('listar_empresas')  # Redireciona para a lista de empresas
    else:
        form = EmpresaForm()
    return render(request, 'core/listar_empresas.html', {'form': form})

def detalhes_empresa(request, empresa_id):
    empresa = get_object_or_404(Empresa, id=empresa_id)
    pedidos = empresa.pedidos.all()
    return render(request, 'core/detalhes_empresa.html', {'empresa': empresa, 'pedidos': pedidos})

def incluir_pedido(request, empresa_id):
    empresa = get_object_or_404(Empresa, id=empresa_id)
    if request.method == 'POST':
        form = PedidoRestituicaoForm(request.POST, request.FILES)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.empresa = empresa
            pedido.save()
            return redirect('detalhes_empresa', empresa_id=empresa.id)
    else:
        form = PedidoRestituicaoForm()
    return render(request, 'core/incluir_pedido.html', {'form': form, 'empresa': empresa})
