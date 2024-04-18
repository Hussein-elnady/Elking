from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    
    # URLs for Products
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('products/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),

    # URLs for Customers
    path('customers/', views.CustomerListView.as_view(), name='customer_list'),
    path('customers/create/', views.CustomerCreateView.as_view(), name='customer_create'),
    path('customers/<int:pk>/update/', views.CustomerUpdateView.as_view(), name='customer_update'),
    path('customers/<int:pk>/delete/', views.CustomerDeleteView.as_view(), name='customer_delete'),

    # URLs for Sales Orders
    path('sales/orders/create/', views.sales_order_create, name='sales_order_create'),
    path('sales/orders/<int:pk>/', views.sales_order_detail, name='sales_order_detail'),
    path('sales/orders/<int:pk>/item/add/', views.sales_order_item_create, name='sales_order_item_create'),
    path('sales/orders/<int:pk>/item/<int:item_pk>/delete/', views.sales_order_item_delete, name='sales_order_item_delete'),
]
