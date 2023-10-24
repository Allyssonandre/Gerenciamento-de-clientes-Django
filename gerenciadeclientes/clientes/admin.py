from django.contrib import admin
from .models import cliente,clienteConta

# CLASSE ADMIN
class Administracao(admin.ModelAdmin):
   readonly_fields = ('field')
   admin.site.site_header = "Gerenciamento de clientes"

# DASHBOARD CLIENTE #
class dashboardCliente(admin.ModelAdmin):
	list_display = ('nomeCliente','dataDaEntrada')
	

admin.site.register(cliente,dashboardCliente)
admin.site.register(clienteConta) 



