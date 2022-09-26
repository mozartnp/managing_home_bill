from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse_lazy, reverse

from backend.apps.purchases.models import DetailedPurchase, Purchase
from backend.apps.purchases.forms import AddingPurchaseForms, UpdatePurchaseForms, AddingDetailedPurchaseForms, UpdateDetailedPurchaseForms

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
    Class View to update a Purchase
    """
    model = Purchase
    template_name = 'purchases/update_purchase.html'
    form_class = UpdatePurchaseForms
    success_url = reverse_lazy('core:listing_purchase')

class AddingDetailedPurchaseCreateView(CreateView):
    """
    Class View to create a new Detailed Purchase
    """
    model = DetailedPurchase
    template_name = 'purchases/adding_detailed_purchase.html'
    form_class = AddingDetailedPurchaseForms

    def get_success_url(self):
        return reverse('core:listing_detailed_purchase', kwargs={"pk" : self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['purchase_pk'] = self.kwargs['pk']
        return context

class ListingDetailedPurchasesListView(ListView):
    """
    Class View to listing all Detailed Purchases
    """
    model = DetailedPurchase
    template_name = 'purchases/listing_detailed_purchases.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['purchase_pk'] = self.kwargs['pk']
        return context

    def get_queryset(self):
        self.purchase = get_object_or_404(Purchase, pk=self.kwargs['pk'])
        return DetailedPurchase.objects.filter(purchase=self.purchase)

class UpdateDetailedPurchaseUpdateView(UpdateView):
    """
    Class View to update a Detailed Purchase
    """
    model = DetailedPurchase
    template_name = 'purchases/update_detailed_purchase.html'
    form_class = UpdateDetailedPurchaseForms

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['purchase_pk'] = self.object.purchase.pk
        return context

    def get_success_url(self):
        return reverse('core:listing_detailed_purchase', kwargs={"pk" : self.object.purchase.pk})
