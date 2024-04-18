from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product, Customer, SalesOrder
from .forms import ProductForm, CustomerForm, SalesOrderForm, SalesOrderItemForm


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main_page')
        else:
            error_message = "Invalid username or password."
            return render(request, 'sales/login.html', {'error_message': error_message})
    return render(request, 'sales/login.html')


def main_page(request):
    return render(request, 'sales/main_page.html')


# Views for Products
class ProductListView(ListView):
    model = Product
    template_name = 'sales/product_list.html'  # Your product list template


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'sales/product_form.html'  # Your product create template
    success_url = reverse_lazy('product_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'sales/product_form.html'  # Your product update template
    success_url = reverse_lazy('product_list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'sales/product_confirm_delete.html'  # Your product delete confirmation template
    success_url = reverse_lazy('product_list')


# Views for Customers
class CustomerListView(ListView):
    model = Customer
    template_name = 'sales/customer_list.html'  # Your customer list template


class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'sales/customer_form.html'  # Your customer create template
    success_url = reverse_lazy('customer_list')


class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'sales/customer_form.html'  # Your customer update template
    success_url = reverse_lazy('customer_list')


class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'sales/customer_confirm_delete.html'  # Your customer delete confirmation template
    success_url = reverse_lazy('customer_list')


# Views for Sales Orders
def sales_order_create(request):
    if request.method == 'POST':
        form = SalesOrderForm(request.POST)
        if form.is_valid():
            sales_order = form.save()
            return redirect('sales_order_detail', pk=sales_order.pk)
    else:
        form = SalesOrderForm()
    return render(request, 'sales/salesorder_form.html', {'form': form})


def sales_order_detail(request, pk):
    sales_order = get_object_or_404(SalesOrder, pk=pk)
    return render(request, 'sales/salesorder_detail.html', {'sales_order': sales_order})


def sales_order_item_create(request, pk):
    sales_order = get_object_or_404(SalesOrder, pk=pk)
    if request.method == 'POST':
        form = SalesOrderItemForm(request.POST)
        if form.is_valid():
            sales_order_item = form.save(commit=False)
            sales_order_item.sales_order = sales_order
            sales_order_item.save()
            return redirect('sales_order_detail', pk=pk)
    else:
        form = SalesOrderItemForm()
    return render(request, 'sales/salesorderitem_form.html', {'form': form})


def sales_order_item_delete(request, pk, item_pk):
    sales_order = get_object_or_404(SalesOrder, pk=pk)
    sales_order_item = get_object_or_404(SalesOrderItem, pk=item_pk)
    if request.method == 'POST':
        sales_order_item.delete()
        return redirect('sales_order_detail', pk=pk)
    return render(request, 'sales/salesorderitem_confirm_delete.html', {'sales_order_item': sales_order_item})
