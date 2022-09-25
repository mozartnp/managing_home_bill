from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class LoginRequiredCustomMixin(LoginRequiredMixin):
    login_url = reverse_lazy('core:login_custom')

