from django import forms
from Task.models import Inventory


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ('item_name', 'item_id', 'description', 'vendor_name', 'photo')