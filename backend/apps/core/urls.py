from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy
from django.views.generic.base import RedirectView

from backend.apps.core.views.userViews import LoginCustomView, TeamChoiceListView, TeamSelectRedirectView
from backend.apps.core.views.basicViews import DashboardView
from backend.apps.core.views.purchasesViews import (
    AddingPurchaseCreateView, ListingPurchasesListView, UpdatePurchaseUpdateView,
    AddingDetailedPurchaseCreateView, ListingDetailedPurchasesListView, UpdateDetailedPurchaseUpdateView
)

app_name = 'core'

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='core:login_custom')),

    path('login/', LoginCustomView.as_view(), name='login_custom'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('core:login_custom')), name='logout_custom'),
    path('team/', TeamChoiceListView.as_view(), name='team_choice'),
    path('team_select/<pk>/', TeamSelectRedirectView.as_view(), name='team_select'),

    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('purchases/addingPurchase/', AddingPurchaseCreateView.as_view(), name='adding_purchase'),
    path('purchases/listingPurchase/', ListingPurchasesListView.as_view(), name='listing_purchase'),
    path('purchases/updatePurchase/<pk>/', UpdatePurchaseUpdateView.as_view(), name='update_purchase'),

    path('purchases/addingDetailedPurchase/<pk>/', AddingDetailedPurchaseCreateView.as_view(), name='adding_detailed_purchase'),
    path('purchases/listingDetailedPurchase/<pk>/', ListingDetailedPurchasesListView.as_view(), name='listing_detailed_purchase'),
    path('purchases/updateDetailedPurchase/<pk>/', UpdateDetailedPurchaseUpdateView.as_view(), name='update_detailed_purchase')
    
]