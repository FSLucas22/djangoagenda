from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# Cria uma tabela com nome core_evento
class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    local = models.CharField(max_length=4000, blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='Data de Criação')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    # Para que o nome da tabela seja "evento" e não "core_evento":
    # class Meta:
    #   db_table = "evento"

    def __str__(self) -> models.CharField:
        return self.titulo
