from django.shortcuts import render,get_object_or_404,  redirect
import time
from .models import cliente,clienteConta
from .forms import Cliente,contaDoCliente

# ***********************PÁGINA INICIAL**************************** #
# ***********************CRIANDO UM CLIENTE************************ #
def index(request):
	qclientes = cliente.objects.count()
	dividasAbertas = clienteConta.objects.count()
	busca = request.GET.get('busca')
	if busca:
		clientes  = cliente.objects.all().filter(nomeCliente__icontains=busca)
	else:
		clientes  = cliente.objects.all().order_by('-dataDaEntrada')[:16]


	pesquisa = request.GET.get('pesquisa')
	if pesquisa:
		conta = clienteConta.objects.all().filter(conta__nomeCliente__icontains=pesquisa)
	else:
		conta = clienteConta.objects.all().order_by('-inicioDaDivida')[:16]	

	Meucliente = Cliente(request.POST or None, request.FILES or None)
	if request.method == 'POST':
		if Meucliente.is_valid():
			obj = Meucliente.save(commit=False)
			obj.save()
			time.sleep(2)
			return redirect('/')
	else:
		Meucliente = Cliente()

	context = {'clientes':clientes, 'qclientes':qclientes,'Meucliente':Meucliente,'conta':conta,'dividasAbertas':dividasAbertas}
	return render(request, 'paginas/index.html',context)

# ****************************************************************** #

# ************************ÁREA DO CLIENTE**************************** #
def ContasApaga(request):
	busca = request.GET.get('busca')
	if busca:
		contas = clienteConta.objects.all().filter(conta__nomeCliente__icontains=busca)
	else:
		contas = clienteConta.objects.all().order_by('-inicioDaDivida')
	contexto = {'contas':contas}
	return render(request, 'paginas/ContasAbertas.html',contexto)
# ****************************************************************** #

# ************************DELETA CLIENTE**************************** #

def deletaCliente(request, id):
	deletandoCliente = get_object_or_404(cliente, pk=id)
	deletandoCliente.delete()
	time.sleep(2)
	return redirect('/')

# ********************************************************************* #
# ************************DETALHEDO CLIENTE**************************** #
def detalheDoCliente(request, id):
	detalharCliente = get_object_or_404(clienteConta,pk=id)
	return render(request, 'paginas/detalheCliente.html',{'detalharCliente':detalharCliente})


# *************************************************************************** #
# ************************CRIAR DÍVIDA DO CLIENTE**************************** # 

def criarDivida(request, id):
	clientedadivida = get_object_or_404(cliente, pk=id)
	divida = contaDoCliente(request.POST or None, request.FILES or None)
	if request.method == 'POST':
		if divida.is_valid():
			d = divida.save(commit=False)
			d.save()
			time.sleep(2)
			return redirect('/')			
	else:
		divida = contaDoCliente()
		return render(request, 'paginas/criarDivida.html', {'divida':divida,'clientedadivida':clientedadivida})

# **************************************************************************** #
# ************************EDIIAR DÍVIDA DO CLIENTE**************************** #

def editarDivida(request, id):
	conta = get_object_or_404(clienteConta,pk=id)
	editaConta = contaDoCliente(instance=conta)
	if(request.method == 'POST'):
		editaConta = contaDoCliente(request.POST,instance=conta)
		if(editaConta.is_valid()):
			conta.save()
			time.sleep(2)
			return redirect('/')
		else:
			return render(request, 'paginas/EditarDivida.html',{'conta':conta,'editaConta':editaConta})
	else:
		return render(request, 'paginas/EditarDivida.html',{'conta':conta,'editaConta':editaConta})

# **************************************************************************** #
# ************************EXCLUIR UM DÍVIDA DO CLIENTE************************ #

def deletaDivida(request,id):
	deletar = get_object_or_404(clienteConta, pk=id)
	deletar.delete()
	time.sleep(2)
	return redirect('/')



	