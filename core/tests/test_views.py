from django import urls
from contextlib import contextmanager
from django.contrib.auth import get_user_model

import pytest
from django.contrib.auth.models import User


@contextmanager
def setup_user(user_data):
    model = get_user_model()
    try:
        user = model.objects.create_user(**user_data)
        yield user
    finally:
        user = model.objects.get(id=user_data['id'])
        if user:
            user.delete()


@pytest.mark.parametrize('url_name', [
    "login",
    "cadastro"
])
def test_not_authenticated_views(client, url_name) -> None:
    url = urls.reverse(url_name)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.parametrize('url_name', [
    "lista_eventos",
    "historico_eventos",
    "evento",
    "logout"
])
def test_authentication_required_views_with_no_auth(client, url_name) -> None:
    url = urls.reverse(url_name)
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
@pytest.mark.parametrize('url_name', [
    "lista_eventos",
    "historico_eventos",
    "evento",
])
def test_after_signin_user_is_authenticated(client, user_sign_in_data, url_name):
    url_cadastro = urls.reverse("submit_cadastro")

    assert User.objects.count() == 0

    response = client.post(url_cadastro, user_sign_in_data)
    assert User.objects.count() == 1
    assert response.status_code == 302

    url = urls.reverse(url_name)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
@pytest.mark.parametrize('url_name', [
    "lista_eventos",
    "historico_eventos",
    "evento",
])
def test_access_as_authenticated_user(client, user_data, url_name) -> None:
    with setup_user(user_data) as user:
        url = urls.reverse(url_name)
        client.force_login(user)
        response = client.get(url)
        assert response.status_code == 200
