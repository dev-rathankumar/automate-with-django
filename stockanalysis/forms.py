from dal import autocomplete
from .models import Stock
from django import forms



class StockForm(forms.Form):
    stock = forms.ModelChoiceField(
        queryset=Stock.objects.all(),
        widget=autocomplete.ModelSelect2(
            url = 'stock_autocomplete',
            attrs={
                'data-placeholder': 'Select a stock..',
            }
        )
    )