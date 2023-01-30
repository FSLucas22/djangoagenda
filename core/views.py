from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email, validate_slug
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.http.response import Http404, JsonResponse
from django.core import validators
from django.db.utils import IntegrityError
from datetime import datetime, timedelta
from . import models

# Create your views here.


# def index(request) -> HttpResponse:
#     return redirect('/agenda/')
from .app_validation import validate_username

requires_login = login_required(login_url="/login/")


def login_user(request) -> HttpResponse:
    return render(request, 'login.html')


def logout_user(request) -> HttpResponse:
    logout(request)
    return redirect('/')


def submit_login(request) -> HttpResponse:
    if not request.POST:
        return redirect('/')

    username = request.POST.get('username')
    print(username)
    password = request.POST.get('password')
    print(request.POST.get)
    print(password)
    usuario = authenticate(username=username, password=password)
    if not usuario:
        messages.error(request, "Usuário ou senha inválido!")
        return redirect('/')

    login(request, usuario)
    return redirect('/')


def get_local(request, titulo_evento: str) -> HttpResponse:
    usuario = request.user
    try:
        evento = models.Evento.objects.get(titulo=titulo_evento)
        if evento.usuario != usuario:
            raise Http404()
        return HttpResponse(evento.local)
    except ObjectDoesNotExist:
        raise Http404()


@requires_login
def index(request) -> HttpResponse:
    return render(request, 'index.html')


@requires_login
def lista_eventos(request) -> HttpResponse:
    usuario = request.user
    data_atual = datetime.now() - timedelta(hours=24)
    eventos = models.Evento.objects.filter(usuario=usuario, data_evento__gte=data_atual)
    dados = {'eventos': eventos}
    return render(request, 'lista.html', dados)


@requires_login
def evento(request) -> HttpResponse:
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        try:
            evento = models.Evento.objects.get(id=id_evento)
        except ObjectDoesNotExist:
            raise Http404()
        if evento.usuario != request.user:
            raise Http404()
        dados['evento'] = models.Evento.objects.get(id=id_evento)
    return render(request, 'evento.html', dados)


@requires_login
def submit_evento(request) -> HttpResponse:
    if not request.POST:
        return redirect('/')

    evento_id = request.POST.get('id')
    titulo = request.POST.get('titulo')
    data_evento = request.POST.get('data')
    local_evento = request.POST.get('local')
    descricao = request.POST.get('descricao')

    usuario = request.user
    if not evento_id:
        models.Evento.objects.create(
            titulo=titulo,
            descricao=descricao,
            data_evento=data_evento,
            local=local_evento,
            usuario=usuario
        )
    else:
        try:
            evento = models.Evento.objects.get(id=evento_id)
            if evento.usuario != usuario:
                raise Http404()
        except ObjectDoesNotExist:
            raise Http404()
        evento.titulo = titulo
        evento.descricao = descricao
        evento.data_evento = data_evento
        evento.local = local_evento
        evento.save()
    return redirect('/')


@requires_login
def delete_evento(request, id_evento: int) -> HttpResponse:
    usuario = request.user
    try:
        evento = models.Evento.objects.get(id=id_evento)
        if evento.usuario != usuario:
            raise Http404()
        evento.delete()
        return redirect('/')
    except ObjectDoesNotExist:
        raise Http404()


@requires_login
def historico_eventos(request) -> HttpResponse:
    usuario = request.user
    data_atual = datetime.now()
    eventos = models.Evento.objects.filter(usuario=usuario, data_evento__lt=data_atual)
    dados = {'eventos': eventos}
    return render(request, 'historico.html', dados)


@requires_login
def json_lista_eventos(request, id_usuario: int) -> HttpResponse:
    usuario = User.objects.get(id=id_usuario)
    eventos = models.Evento.objects.filter(usuario=usuario).values('id', 'titulo')
    return JsonResponse(list(eventos), safe=False)


def cadastro_usuario(request) -> HttpResponse:
    return render(request, 'cadastro.html')


def submit_usuario(request) -> HttpResponse:
    if not request.POST:
        return redirect('/')
    try:
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        email = request.POST.get('email')

        validate_username(nome)
        validate_email(email)
        validate_password(senha, nome)

        if User.objects.filter(username=nome).exists():
            messages.error(request, "O nome de usuário já existe."
            " Caso já possua uma conta, tente <a href='/login'>fazer login</a>."
            )
            return redirect('/cadastro')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Este email já está cadastrado. "
                                    " Caso já possua uma conta, tente <a href='/login'>fazer login</a>.")
            return redirect('/cadastro')

        User.objects.create_user(nome, email, senha)
        messages.success(request, "Usuário cadastrado com sucesso!")
        return redirect('/cadastro')

    except IntegrityError as e:
        print(e)
        messages.error(request, "Algo deu errado. Por favor tente novamente.")
        return redirect('/cadastro')

    except ValidationError as e:
        for message in e.messages:
            messages.error(request, message)
        return redirect('/cadastro')
