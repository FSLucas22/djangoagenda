from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

from core.rules.constants import TipoRepeticao, PARA_SEMPRE


# Create your models here.


class RegraRepeticao(models.Model):
    tipo_regra = models.IntegerField(choices=TipoRepeticao.choices)
    vezes = models.IntegerField(default=PARA_SEMPRE)
    periodo = models.DateTimeField(blank=True, null=True)
    flag_fevereiro_29 = models.BooleanField(default=False)
    flag_ir_para_marco = models.BooleanField(default=False)


# Cria uma tabela com nome core_evento
class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    local = models.CharField(max_length=4000, blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='Data de Criação')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    regra_repeticao = models.ForeignKey(RegraRepeticao, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> models.CharField:
        return self.titulo

    def get_data_evento(self) -> str:
        return self.data_evento.strftime('%d/%m/%Y %Hh%Mmin')

    def get_data_evento_input(self) -> str:
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')

    def get_evento_atrasado(self) -> bool:
        data_atual = datetime.now()
        return self.data_evento < data_atual

    def get_minutes_to_evento(self) -> float:
        data_atual = datetime.now()
        delta = self.data_evento - data_atual
        minutes = delta.total_seconds() / 60
        return minutes


