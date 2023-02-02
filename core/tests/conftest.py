import pytest


@pytest.fixture
def user_name() -> str:
    return "user1"


@pytest.fixture
def user_email() -> str:
    return 'user@email.com'


@pytest.fixture
def user_password() -> str:
    return 'user_12345'


@pytest.fixture
def user_sign_in_data(user_name, user_email, user_password) -> dict[str, str]:
    return {
        "username": user_name,
        "email": user_email,
        "password1": user_password,
        "password2": user_password
    }


@pytest.fixture
def user_data(user_name, user_email, user_password) -> dict[str, str]:
    return {
        'id': -1,
        'username': user_name,
        'email': user_email,
        'password': user_password,
    }
