from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import (
    ListView, 
    DetailView, 
    RedirectView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.shortcuts import render, get_object_or_404

from .forms import ProductModelForm 
from .mixins import TemplateTitleMixin
from .models import Product, DigitalProduct

class ProtectedProductUpdateView(LoginRequiredMixin,UpdateView):
    form_class = ProductModelForm
    template_name = "products/product_detail.html"

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)

    def get_success_url(self):
        return self.object.get_edit_url()
    
class ProtectedProductDeleteView(LoginRequiredMixin,DeleteView):
    template_name = "products/forms-delete.html"

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)

    def get_success_url(self):
        return "/products/products"

class ProtectedProductCreateView(LoginRequiredMixin,CreateView):
    form_class = ProductModelForm
    template_name = "products/forms.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)
    

class ProductIDRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        url_params = self.kwargs
        pk = url_params.get("pk")
        obj = get_object_or_404(Product, pk=pk)
        slug = obj.slug
        return f"/products/products/{slug}"

class ProductRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        url_params = self.kwargs
        slug = url_params.get("slug")
        return f"/products/products/{slug}"

class DigitalProductListView(TemplateTitleMixin, ListView):
    model = DigitalProduct
    template_name = "products/product_list.html"
    title = "Productos Digitales"
    
class ProductListView(TemplateTitleMixin, ListView):
    # app_label = 'products'
    # model = Product
    # view_name = list
    # template_name = <app_name>/<model>_<view_name>.html
    # template_name = 'products/product_list.html'
    model = Product
    title = "Productos Fisicos"    

class ProductDetailView(DetailView):
    model = Product

class ProtectedProductDetailView(LoginRequiredMixin, DetailView):
    model = Product