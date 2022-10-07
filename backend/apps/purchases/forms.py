from django import forms

from backend.apps.purchases.models import DetailedPurchase, Purchase
from backend.apps.customUser.models import CustomUserModels, TeamModel

class AddingPurchaseForms(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=CustomUserModels.objects.all(), widget=forms.HiddenInput())
    team = forms.ModelChoiceField(queryset=TeamModel.objects.all(), widget=forms.HiddenInput()) 

    class Meta:
        model = Purchase
        localized_fields = ('purchaseValue',)
        fields = [
            'purchaseName',
            'placePurchase',
            'isDetailedPurchase',
            'purchaseValue',
            'typePayment',
            'note',
            'user',
            'team'
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
            "isDetailedPurchase" : forms.CheckboxInput(attrs={"onclick": "checkisDetailedPurchase()"}),
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
        localized_fields = ('purchaseValue',)
        fields = [
            'purchaseName',
            'placePurchase',
            'isDetailedPurchase',
            'purchaseValue',
            'typePayment',
            'note'
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
            "isDetailedPurchase" : forms.CheckboxInput(attrs={"onclick": "checkisDetailedPurchase()"}),
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

class AddingDetailedPurchaseForms(forms.ModelForm):
    purchase = forms.ModelChoiceField(queryset=Purchase.objects.all(), widget=forms.HiddenInput())
    user = forms.ModelChoiceField(queryset=CustomUserModels.objects.all(), widget=forms.HiddenInput())
    team = forms.ModelChoiceField(queryset=TeamModel.objects.all(), widget=forms.HiddenInput()) 

    class Meta:
        model = DetailedPurchase
        localized_fields = ('amount','price',)
        fields = [
            'productName',
            'amount',
            'price',
            'purchase', #TODO ? Preciso do campo que está como hiddeninput aqui?
            'user',
            'team'
        ]
        labels = {
            'productName' : 'Nome do Produto',
            'amount' : 'Quantidade',
            'price' : 'Preço'
        }
        widgets= {
            'productName' : forms.TextInput(attrs={'placeholder': 'Digite o nome do produto'})
        }

    def __init__(self, *args, **kwargs):
        super(AddingDetailedPurchaseForms, self).__init__(*args, **kwargs)
        self.fields['amount'].required = False

class UpdateDetailedPurchaseForms(forms.ModelForm):

    class Meta:
        model = DetailedPurchase
        localized_fields = ('amount','price',)
        fields = [
            'productName',
            'amount',
            'price'
        ]
        labels = {
            'productName' : 'Nome do Produto',
            'amount' : 'Quantidade',
            'price' : 'Preço'
        }
        widgets= {
            'productName' : forms.TextInput(attrs={'placeholder': 'Digite o nome do produto'})
        }

    def __init__(self, *args, **kwargs):
        super(UpdateDetailedPurchaseForms, self).__init__(*args, **kwargs)
        self.fields['productName'].required = False
        self.fields['amount'].required = False
        self.fields['price'].required = False