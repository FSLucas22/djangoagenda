from core import models
from core.rules import constants


def criar_evento(request) -> models.Evento:
    evento = models.Evento.objects.create(
        titulo=request.POST.get('titulo'),
        data_evento=request.POST.get('data'),
        local=request.POST.get('local'),
        descricao=request.POST.get('descricao'),
        usuario=request.user
    )
    if request.POST.get('repetir'):
        regra = criar_regra(request)
        evento.regra_repeticao = regra
        evento.save()
    return evento


def criar_regra(request) -> models.RegraRepeticao:
    tipo_regra = request.POST.get('regra')
    data = request.POST.get('data')
    fevereiro_29 = False
    ir_para_marco = bool(request.POST.get('ir_para_marco'))
    vezes = request.POST.get('vezes')
    if tipo_regra == "TODO_ANO":
        if data.month == 2 and data.day == 29:
            fevereiro_29 = True
    return models.RegraRepeticao.objects.create(
        tipo_regra=constants.TipoRepeticao[tipo_regra],
        vezes=vezes if vezes else constants.PARA_SEMPRE,
        flag_fevereiro_29=fevereiro_29,
        flag_ir_para_marco=ir_para_marco
    )
