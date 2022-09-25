from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse_lazy

from backend.apps.purchases.models import Purchase
from backend.apps.purchases.forms import AddingPurchaseForms, UpdatePurchaseForms

class AddingPurchaseCreateView(CreateView):
    """
    Class View to create a new Purchase
    """
    model = Purchase
    template_name = 'purchases/adding_purchase.html'
    form_class = AddingPurchaseForms
    success_url = reverse_lazy('core:listing_purchase')

class ListingPurchasesListView(ListView):
    """
    Class View to listing all Purchases
    """
    model = Purchase
    template_name = 'purchases/listing_purchases.html'
    paginate_by = 10

class UpdatePurchaseUpdateView(UpdateView):
    """
    Class View to listing a Purchase
    """
    model = Purchase
    template_name = 'purchases/update_purchase.html'
    form_class = UpdatePurchaseForms
    success_url = reverse_lazy('core:listing_purchase')