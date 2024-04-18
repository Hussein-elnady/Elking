from django import forms
from .models import Product, Customer, SalesOrder


class ProductForm(forms.ModelForm):
    """
    Form for creating and editing products.
    """

    class Meta:
        model = Product
        fields = ['name', 'description', 'unit', 'price', 'category']


class CustomerForm(forms.ModelForm):
    """
    Form for creating and editing customers.
    """

    class Meta:
        model = Customer
        fields = ['name', 'contact_name', 'email', 'phone_number']


class SalesOrderForm(forms.ModelForm):
    """
    Form for creating and editing sales orders.
    """

    class Meta:
        model = SalesOrder
        exclude = ['date']  # Exclude the non-editable field 'date'


class SalesOrderItemForm(forms.Form):
    """
    Form for adding/editing individual sales order items.
    This form is not a ModelForm as it doesn't directly save to a model.
    """
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    quantity = forms.IntegerField(min_value=1)
    unit_price = forms.DecimalField(max_digits=10, decimal_places=2)
