from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_empresas, name='listar_empresas'),
    path('cadastrar/', views.cadastrar_empresa, name='cadastrar_empresa'),
    path('<int:empresa_id>/', views.detalhes_empresa, name='detalhes_empresa'),
    path('<int:empresa_id>/incluir_pedido/', views.incluir_pedido, name='incluir_pedido'),
]
