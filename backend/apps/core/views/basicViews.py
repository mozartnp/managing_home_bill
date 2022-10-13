from django.views.generic import TemplateView

from backend.apps.core.mixins import LoginRequiredCustomMixin, TeamMixin

class DashboardView(LoginRequiredCustomMixin, TeamMixin, TemplateView):
    template_name = "basic/dashboard.html"