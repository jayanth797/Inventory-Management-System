from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .forms import ProductForm
from .serializers import ProductSerializer

@login_required
def product_list(request):
    query = request.GET.get('q')

    if query:
        products_queryset = Product.objects.filter(user=request.user, name__icontains=query)
    else:
        products_queryset = Product.objects.filter(user=request.user)

    paginator = Paginator(products_queryset, 5)  # 5 items per page
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    return render(request, 'product_list.html', {'products': products, 'query': query})

@login_required
def add_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return redirect('product_list')
    return render(request, 'add_product.html', {'form': form})

@login_required
def update_product(request, id):
    product = get_object_or_404(Product, id=id, user=request.user)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'update_product.html', {'form': form})

@login_required
@require_POST
def delete_product(request, id):
    product = get_object_or_404(Product, id=id, user=request.user)
    product.delete()
    return redirect('product_list')

@login_required
def dashboard(request):
    products = Product.objects.filter(user=request.user)

    total_products = products.count()
    total_quantity = products.aggregate(Sum('quantity'))['quantity__sum'] or 0
    total_value = sum([p.quantity * p.price for p in products])

    low_stock = products.filter(quantity__lt=5)

    # Chart Data
    product_names = [p.name for p in products]
    product_values = [p.quantity * p.price for p in products]
    product_quantities = [p.quantity for p in products]

    context = {
        'total_products': total_products,
        'total_quantity': total_quantity,
        'total_value': total_value,
        'low_stock': low_stock,
        'names': product_names,
        'values': product_values,
        'quantities': product_quantities,
    }

    return render(request, 'dashboard.html', context)

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)