from django import forms
from .models import Product, Customer, SalesOrder, SalesOrderItem, Category


class ProductForm(forms.ModelForm):
    """
    Form for creating and editing products.
    """

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        help_text="Select the category for this product."
    )

    class Meta:
        model = Product
        fields = ['code', 'name', 'description', 'unit', 'price', 'category']
        help_texts = {
            'code': 'Enter a unique code for the product.',
            'name': 'Enter the name of the product.',
            'description': 'Enter a description of the product (optional).',
            'unit': 'Enter the unit of measurement for the product (e.g., kg, ton).',
            'price': 'Enter the price per unit of the product.',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['code'].disabled = False  # Make the code field read-only

    def clean(self):
        cleaned_data = super().clean()
        # Add custom validation logic if needed
        return cleaned_data


class CustomerForm(forms.ModelForm):
    """
    Form for creating and editing customers.
    """

    class Meta:
        model = Customer
        fields = ['name', 'contact_name', 'email', 'phone_number']
        help_texts = {
            'name': 'Enter the name of the customer.',
            'contact_name': 'Enter the name of the primary contact person for the customer.',
            'email': 'Enter the email address of the customer.',
            'phone_number': 'Enter the phone number of the customer.',
        }


class SalesOrderForm(forms.ModelForm):
    """
    Form for creating and editing sales orders.
    """

    class Meta:
        model = SalesOrder
        fields = ['customer']  # Excluding 'items' as it's managed dynamically
        help_texts = {
            'customer': 'Select the customer who placed the sales order.',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].queryset = Customer.objects.all()


class SalesOrderItemForm(forms.ModelForm):
    """
    Form for adding/editing individual sales order items.
    """

    class Meta:
        model = SalesOrderItem
        fields = ['product', 'quantity', 'unit_price']
        widgets = {
            'product': forms.Select(attrs={'class': 'select2'}),
        }
        help_texts = {
            'product': 'Select the product to include in the sales order.',
            'quantity': 'Enter the quantity of the product for the sales order.',
            'unit_price': 'Enter the unit price of the product for the sales order.',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].queryset = Product.objects.all()
