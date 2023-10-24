from django.contrib import admin
from django.urls import path, include
# IMPORT DAS CONFIGURAÇÕES DA IMAGEM
from django.conf import settings
from django.contrib.auth import views as auth_views
# ------------------------------------
# CAMINHO DA IMAGEM, IMPORTANDO O STATIC
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('clientes.urls')),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) # imagem de perfil
