from django.urls import path

from . import views

urlpatterns = [
	path('',views.index, name="index"),
	path('deleta/<int:id>',views.deletaCliente, name="deleta"),
	path('detalhecliente/<int:id>',views.detalheDoCliente, name="detalhecliente"),
	path('criar-divida/<int:id>', views.criarDivida, name="criardivida"),
	path('editar-Divida/<int:id>', views.editarDivida,name="editar-Divida"),
	path('deletando-Divida/<int:id>',views.deletaDivida, name="deletando-Divida"),
	path('Contas/',views.ContasApaga,name="Contas"),	
] 