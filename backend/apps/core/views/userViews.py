from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.views.generic import FormView, ListView
from django.urls import reverse_lazy

from backend.apps.custom_user.forms import TeamChoiceForms
from backend.apps.custom_user.models import CustomUserModels

class LoginCustomView(LoginView):
    """
    Class View para Login de User
    """
    template_name = 'user/login.html'
    success_url = reverse_lazy('core:dashboard')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)

# class TeamChoiceFormView(FormView):
#     """
#     Class View to set a team.
#     """
#     template_name = 'user/team.html'
#     form_class = TeamChoiceForms

#     def get_form_kwargs(self):
#         kwargs = super(TeamChoiceFormView, self).get_form_kwargs()
#         kwargs['user'] = self.request.user
#         return kwargs

class TeamChoiceListView(ListView):
    """
        Class View to set a team.
    """
    template_name = 'user/team.html'
    model = CustomUserModels

    def get_queryset(self):
        queryset = self.request.user.team.all()
        print(queryset)
        return queryset