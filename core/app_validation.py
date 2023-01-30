from typing import Type

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import validate_slug
from django.utils.translation import gettext_lazy as _
from django.db import models


def validate_username(nome: str):
    validate_slug(nome)
    messages = []
    if len(nome) < 5:
        messages.append("O nome de usuário deve conter ao menos 5 caracteres")
    if len(nome) > 20:
        messages.append("O nome de usuário deve conter no máximo 20 caracteres")
    if not nome[0].isalpha():
        messages.append("O nome de usuário deve começar com uma letra")
    if len(messages) > 0:
        raise ValidationError(_(" ".join(messages)))


def validate_unique(field: str, model: Type[models.Model] | Type[AbstractUser], field_name: str | None = None):
    if not field_name:
        field_name = field

    def check(value):
        data = {field: value}
        if model.objects.filter(**data).exists():
            raise ValidationError(_("%(field_name)s já existe"), params={"field_name": field_name.capitalize()})

    return check