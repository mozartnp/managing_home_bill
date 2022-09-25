from django import forms

from backend.apps.purchases.models import Purchase

class AddingPurchaseForms(forms.ModelForm):

    class Meta:
        model = Purchase
        fields = [
            'purchaseName', 'placePurchase', 'isDetailedPurchase', 'purchaseValue', 'typePayment', 'note'
        ]
        labels = {
            'purchaseName' : 'Compra',
            'placePurchase' : 'Local da Compra',
            'isDetailedPurchase' : 'Compra detalhada',
            'typePayment': 'Tipo de pagamento',
            'note' : 'Observação',
            'purchaseValue' : 'Valor da compra'
        }
        widgets= {
            "isDetailedPurchase" : forms.CheckboxInput(),
            'purchaseName' : forms.TextInput(attrs={'placeholder': 'Digite o nome da compra'}),
            'placePurchase' : forms.TextInput(attrs={'placeholder': 'Digite o local de compra'}),
            'typePayment' : forms.TextInput(attrs={'placeholder': 'Digite o tipo de pagamento'}),
            'note' : forms.TextInput(attrs={'placeholder': 'Digite observações adicionais'})            
        }

    def __init__(self, *args, **kwargs):
        super(AddingPurchaseForms, self).__init__(*args, **kwargs)
        self.fields['placePurchase'].required = False
        self.fields['isDetailedPurchase'].required = False
        self.fields['purchaseValue'].required = False
        self.fields['typePayment'].required = False
        self.fields['note'].required = False


class UpdatePurchaseForms(forms.ModelForm):

    class Meta:
        model = Purchase
        fields = [
            'purchaseName', 'placePurchase', 'isDetailedPurchase', 'purchaseValue', 'typePayment', 'note'
        ]
        labels = {
            'purchaseName' : 'Compra',
            'placePurchase' : 'Local da Compra',
            'isDetailedPurchase' : 'Compra detalhada',
            'typePayment': 'Tipo de pagamento',
            'note' : 'Observação',
            'purchaseValue' : 'Valor da compra'
        }
        widgets= {
            "isDetailedPurchase" : forms.CheckboxInput(),
            'purchaseName' : forms.TextInput(attrs={'placeholder': 'Digite o nome da compra'}),
            'placePurchase' : forms.TextInput(attrs={'placeholder': 'Digite o local de compra'}),
            'typePayment' : forms.TextInput(attrs={'placeholder': 'Digite o tipo de pagamento'}),
            'note' : forms.TextInput(attrs={'placeholder': 'Digite observações adicionais'})            
        }

    def __init__(self, *args, **kwargs):
        super(UpdatePurchaseForms, self).__init__(*args, **kwargs)
        self.fields['purchaseName'].required = False
        self.fields['placePurchase'].required = False
        self.fields['isDetailedPurchase'].required = False
        self.fields['purchaseValue'].required = False
        self.fields['typePayment'].required = False
        self.fields['note'].required = False
