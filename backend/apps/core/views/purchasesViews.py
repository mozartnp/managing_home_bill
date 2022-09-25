from django.views.generic import CreateView
from django.urls import reverse_lazy

from backend.apps.purchases.models import Purchase
from backend.apps.purchases.forms import AddingPurchaseForms

class AddingPurchaseCreateView(CreateView):
    """
    Class View do create a new Purchase
    """
    model = Purchase
    template_name = 'purchases/adding_purchase.html'
    form_class = AddingPurchaseForms
    success_url = reverse_lazy('core:dashboard') #TODO arrumar o redirecionamento