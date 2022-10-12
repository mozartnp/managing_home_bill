from django.views.generic import TemplateView

from backend.apps.core.mixins import LoginRequiredCustomMixin
from backend.apps.custom_user.models import TeamModel

class DashboardView(LoginRequiredCustomMixin, TemplateView):
    template_name = "basic/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team'] = TeamModel.objects.filter(pk=self.request.session['team_pk']).first() # TODO passar esse contexto em mixin
        return context