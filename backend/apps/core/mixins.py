from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from backend.apps.custom_user.models import TeamModel

class LoginRequiredCustomMixin(LoginRequiredMixin):
    login_url = reverse_lazy('core:login_custom')

class TeamMixin:
    fail_url = reverse_lazy('core:team_choice')

    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('team_pk'):
            return HttpResponseRedirect(self.fail_url)
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team'] = TeamModel.objects.filter(pk=self.request.session.get('team_pk')).first()
        return context
