from django.views.generic import TemplateView

from backend.apps.core.mixins import LoginRequiredCustomMixin

class DashboardView(LoginRequiredCustomMixin, TemplateView):
    template_name = "basic/dashboard.html"