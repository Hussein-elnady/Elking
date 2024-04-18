from django.db import models

class Product(models.Model):
  """
  Model representing a food commodity traded by the company.
  """
  name = models.CharField(max_length=100)
  description = models.TextField()
  unit = models.CharField(max_length=50)  # Unit (e.g., kg, ton)
  price = models.DecimalField(max_digits=10, decimal_places=2)  # Price per unit
  category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)  # Optional foreign key to a Category model (if needed)

  def __str__(self):
    return self.name

class Category(models.Model):
  """
  Optional model to categorize products (e.g., Grains, Fruits, Vegetables).
  """
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name

class Customer(models.Model):
  """
  Model representing a customer company.
  """
  name = models.CharField(max_length=100)
  contact_name = models.CharField(max_length=50)
  email = models.EmailField()
  phone_number = models.CharField(max_length=20)
  # Add other relevant fields as needed (address, payment terms, etc.)

  def __str__(self):
    return self.name

class SalesOrder(models.Model):
  """
  Model representing a sales order placed by a customer.
  """
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
  date = models.DateField(auto_now_add=True)
  # Many-to-many relationship with Product model (implemented through a separate table)
  items = models.ManyToManyField(Product, through='SalesOrderItem')
  total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

  def __str__(self):
    return f"Sales Order - {self.id} - {self.customer}"

class SalesOrderItem(models.Model):
  """
  Model representing a specific product quantity within a SalesOrder.
  This model connects the SalesOrder and Product models with additional details.
  """
  sales_order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.PositiveIntegerField()
  unit_price = models.DecimalField(max_digits=10, decimal_places=2)
  # Additional fields as needed (discount, etc.)

  def __str__(self):
    return f"{self.quantity}x {self.product} ({self.sales_order})"
