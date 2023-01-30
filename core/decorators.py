from django.shortcuts import redirect


def user_not_authenticated(function=None, redirect_url='/'):
    """
    Decorator para views que checa se o usuário não está autenticado, redirecionando
    para a página inicial se necessário por padrão.
    """
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_url)

            return view_func(request, *args, **kwargs)

        return _wrapped_view

    if function:
        return decorator(function)

    return decorator