from django import forms
from .models import *
from .models import cliente, clienteConta

# *************************** FORM CLIENTE ************************ #
class Cliente(forms.ModelForm):
    class Meta:
        model  = cliente
        fields = 'nomeCliente',
# ***************************************************************** # 

# ************************** FORM DA CONTA DO CLIENTE ************* #
class contaDoCliente(forms.ModelForm):
    descricao = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    class Meta:
        model  = clienteConta
        fields = 'conta','divida','descricao',
# ***************************************************************** # 