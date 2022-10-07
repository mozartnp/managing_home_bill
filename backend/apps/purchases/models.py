from django.conf import settings
from django.db import models

from backend.apps.custom_user.models import TeamModel
from backend.apps.core.models import DateModel

class Purchase(DateModel):
    purchaseName = models.CharField(max_length=200)
    placePurchase = models.CharField(max_length=200, null=True)
    isDetailedPurchase = models.BooleanField()
    purchaseValue = models.FloatField(null=True)
    typePayment = models.CharField(max_length=200, null=True)
    note = models.CharField(max_length=500, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    team = models.ForeignKey(TeamModel, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.purchaseName} {self.created}"

class DetailedPurchase(DateModel):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    productName = models.CharField(max_length=200)
    amount = models.FloatField(default=1)
    price = models.FloatField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    team = models.ForeignKey(TeamModel, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
            return f"{self.productName} / {self.purchase}"
    