from django.db import models

from backend.apps.core.models import DateModel

class Purchase(DateModel):
    purchaseName = models.CharField(max_length=200)
    placePurchase = models.CharField(max_length=200, null=True)
    isDetailedPurchase = models.BooleanField()
    purchaseValue = models.FloatField()
    typePayment = models.CharField(max_length=200, null=True)
    note = models.CharField(max_length=500, null=True)

class DetailedPurchase(DateModel):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    productName = models.CharField(max_length=200)
    amount = models.FloatField()
    price = models.FloatField()