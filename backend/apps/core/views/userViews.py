from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.views.generic import FormView, ListView, RedirectView
from django.urls import reverse_lazy

from backend.apps.custom_user.models import CustomUserModels

class LoginCustomView(LoginView):
    """
    Class View para Login de User
    """
    template_name = 'user/login.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)

class TeamChoiceListView(ListView):
    """
        Class View to set a team.
    """
    template_name = 'user/team.html'
    model = CustomUserModels

    def get_queryset(self):
        queryset = self.request.user.team.all()
        return queryset

class TeamSelectRedirectView(RedirectView):
    """
        Class View to set team on sessions
    """
    url = reverse_lazy('core:dashboard')

    def dispatch(self, request, *args, **kwargs):
        request.session['team_pk'] = kwargs['pk']
        return super().dispatch(request, *args, **kwargs)