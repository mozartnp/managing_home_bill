from django.contrib.auth.views import LoginView

class LoginCustomView(LoginView):
    """
    Class View para Login de User
    """
    template_name = 'user/login.html'