from django.core.exceptions import ValidationError
from django.core.validators import validate_slug
from django.utils.translation import gettext_lazy as _

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
