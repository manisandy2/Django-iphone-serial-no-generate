from django import forms
from .models import Product_List
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.utils.translation import gettext, gettext_lazy as _


class LogInForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, "class": 'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.TextInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}
    ))


class ProductListForm(forms.ModelForm):
    class Meta:
        model = Product_List
        fields = ['list_of_name', 'list_of_code', 'list_of_range', "name_invoice_create", "invoice"]
        widgets = {
            "list_of_name": forms.Select({"name": "select_0", "class": "form-control"}),
            "list_of_code": forms.TextInput(attrs={"class": "form-control", "placeholder": "Code"}),
            "list_of_range": forms.TextInput(attrs={"class": "form-control", "placeholder": "Range"}),
            "name_invoice_create": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter you Name"}),
            "invoice": forms.TextInput(attrs={"class": "form-control", "placeholder": "Invoice Number"}),
        }
