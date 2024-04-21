from django.contrib import admin
from .models import Product, Category, Customer, SalesOrder, SalesOrderItem

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(SalesOrder)
admin.site.register(SalesOrderItem)
