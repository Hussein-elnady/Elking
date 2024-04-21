from django.urls import path
from . import views
from .views import product_list, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = 'sales'  # Add namespace
'''
urlpatterns = [
    path('', views.main_page, name='main_page'),

    # URLs for Products

    # path('products/', views.ProductListView.as_view(), name='product_list'),
    # path('products/create/', views.ProductCreateView.as_view(), name='product_create'),
    # path('products/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product_update'),
    # path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),

    # URLs for Customers
    # path('customers/', views.CustomerListView.as_view(), name='customer_list'),
    # path('customers/create/', views.CustomerCreateView.as_view(), name='customer_create'),
    # path('customers/<int:pk>/update/', views.CustomerUpdateView.as_view(), name='customer_update'),
    # path('customers/<int:pk>/delete/', views.CustomerDeleteView.as_view(), name='customer_delete'),

    # URLs for Sales Orders
    # path('sales/orders/create/', views.sales_order_create, name='sales_order_create'),
    # path('sales/orders/<int:pk>/', views.sales_order_detail, name='sales_order_detail'),
    # path('sales/orders/<int:pk>/item/add/', views.sales_order_item_create, name='sales_order_item_create'),
    # path('sales/orders/<int:pk>/item/<int:item_pk>/delete/', views.sales_order_item_delete, name='sales_order_item_delete'),

    path('products/', product_list, name='product_list'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
]
'''


urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('login/', views.login_view, name='login'),

    path('products/', views.product_list, name='product_list'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('products/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),

    path('customers/', views.customer_list, name='customer_list'),

    path('create-sales-order/', views.create_sales_order, name='create_sales_order'),
    path('sales-order/<int:pk>/', views.sales_order_detail, name='sales_order_detail'),
]
