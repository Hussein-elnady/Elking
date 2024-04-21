from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Product, Customer, SalesOrder, SalesOrderItem
from .forms import ProductForm, CustomerForm, SalesOrderForm, SalesOrderItemForm


def login_view(request):
    """
    View for user login.
    """
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


@login_required
def main_page(request):
    """
    View for the main page.
    """
    return render(request, 'sales/main_page.html')


# ------------------------------ Product ------------------------------ #
class ProductCreateView(LoginRequiredMixin, CreateView):
    """
    View for creating a new product.
    """
    model = Product
    form_class = ProductForm
    template_name = 'sales/product_create.html'
    success_url = reverse_lazy('sales:product_list')


@login_required
def product_list(request):
    """
    View for listing all products.
    """
    # Fetch all products from the database
    products = Product.objects.all()

    # Handle search functionality
    search_query = request.GET.get('search')
    if search_query:
        # Filter products based on name or code containing the search query
        products = products.filter(name__icontains=search_query) | products.filter(code__icontains=search_query)

    # Render the product list template with the fetched products
    return render(request, 'sales/product_list.html', {'products': products})


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """
    View for updating a product.
    """
    model = Product
    form_class = ProductForm
    template_name = 'sales/product_update.html'
    success_url = reverse_lazy('sales:product_list')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """
    View for deleting a product.
    """
    model = Product
    template_name = 'sales/product_confirm_delete.html'
    success_url = reverse_lazy('sales:product_list')


@login_required
def product_detail(request, pk):
    """
    View for displaying details of a product.
    """
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'sales/product_detail.html', {'product': product})


# ------------------------------ Customer ------------------------------ #
@login_required
class CustomerCreateView(LoginRequiredMixin, CreateView):
    """
    View for creating a new customer.
    """
    model = Customer
    form_class = CustomerForm
    template_name = 'sales/customer_create.html'
    success_url = reverse_lazy('sales:customer_list')

@login_required
def customer_list(request):
    """
    View for listing all customers.
    """
    customers = Customer.objects.all()
    return render(request, 'sales/customer_list.html', {'customers': customers})


@login_required
def create_sales_order(request):
    """
    View for creating a new sales order.
    """
    if request.method == 'POST':
        form = SalesOrderForm(request.POST)
        if form.is_valid():
            sales_order = form.save(commit=False)
            sales_order.save()
            form.save_m2m()
            return redirect('sales:sales_order_detail', pk=sales_order.pk)
    else:
        form = SalesOrderForm()
    return render(request, 'sales/create_sales_order.html', {'form': form})


@login_required
def sales_order_detail(request, pk):
    """
    View for displaying details of a sales order.
    """
    sales_order = get_object_or_404(SalesOrder, pk=pk)
    return render(request, 'sales/sales_order_detail.html', {'sales_order': sales_order})
