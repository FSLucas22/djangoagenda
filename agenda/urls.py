"""agenda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from core import views

app_name = 'agenda'
urlpatterns = [
    path('', views.index, name="index"),
    path('evento/<titulo_evento>/', views.get_local),
    path('agenda/', views.lista_eventos, name="lista_eventos"),
    path('agenda/historico/', views.historico_eventos, name="historico_eventos"),
    path('agenda/lista/<int:id_usuario>/', views.json_lista_eventos),
    path('agenda/evento/', views.evento, name="evento"),
    path('agenda/evento/submit', views.submit_evento),
    path('agenda/evento/delete/<int:id_evento>/', views.delete_evento, name="delete_evento"),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('cadastro/', views.cadastro_usuario),
    path('cadastro/submit', views.submit_usuario),
    path('logout/', views.logout_user, name="logout"),
    path('admin/', admin.site.urls),
]
