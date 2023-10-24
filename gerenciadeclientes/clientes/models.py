from django.db import models
import datetime
from django.contrib.auth.models import User

# ***************************************** CLASSE DOS CLIENTES ************************************************* #
class cliente(models.Model):
    nomeCliente   = models.CharField(max_length=100, null="false", blank="false",verbose_name="Nome do cliente")
    dataDaEntrada = models.DateTimeField(auto_now_add=True, verbose_name='Entrou:')
    update        = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.nomeCliente;
# **************************************************************************************************************** #      

# ******************************************** CLASSE DA CONTA DOS CLIENTES ************************************** #
class clienteConta(models.Model):
    conta           = models.ForeignKey(cliente,null=True, blank=True,on_delete=models.CASCADE, verbose_name='Conta do cliente:')
    divida          = models.DecimalField(max_digits=5, decimal_places=2)
    descricao       = models.CharField(max_length=200, null="false", blank="false",verbose_name="Descrição da dívida:") 
    inicioDaDivida  = models.DateTimeField(auto_now_add=True, verbose_name="Começo da dívida")
    mudancaDaDivida = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.conta.nomeCliente;
# **************************************************************************************************************** #      






