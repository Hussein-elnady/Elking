from django.db import models


# ------------------------------  Product ------------------------------ #

class Product(models.Model):
    """
    Model representing a food commodity traded by the company.
    """
    UNIT_CHOICES = [
        ('kg', 'Kilogram'),
        ('g', 'Gram'),
        ('ton', 'Ton'),
    ]

    code = models.CharField(max_length=20, unique=True, primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    unit = models.CharField(max_length=50, choices=UNIT_CHOICES, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, related_name='products')

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    Optional model to categorize products (e.g., Grains, Fruits, Vegetables).
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# ------------------------------ Customer ------------------------------ #

class Customer(models.Model):
    """
    Model representing a customer company.
    """
    name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# ------------------------------ SalesOrder ------------------------------ #

class SalesOrder(models.Model):
    """
    Model representing a sales order placed by a customer.
    """
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    date = models.DateField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Sales Order - {self.id} - {self.customer}"


# ------------------------------ SalesOrderItem ------------------------------ #
class SalesOrderItem(models.Model):
    """
    Model representing a specific product quantity within a SalesOrder.
    """
    sales_order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity}x {self.product} ({self.sales_order})"
