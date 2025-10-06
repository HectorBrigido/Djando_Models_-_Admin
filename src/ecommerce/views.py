from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductModelForm
from .models import ProductModel

def product_model_list_view(request):
    query = request.GET.get("q", None)
    queryset = ProductModel.objects.all()
    if query is not None:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )
    template = "layouts/ecommerce/list-view.html"
    context = {"products": queryset}
    return render(request, template, context)

def product_model_delete_view(request, product_id):
    instance = get_object_or_404(ProductModel, id=product_id)
    if request.method == "POST":
        instance.delete()
        messages.success(request, "Producto eliminado con éxito")
        return redirect("list")
    
    context= {"product": instance }
    template = "layouts/ecommerce/delete-view.html"
    return render(request, template, context)

# @login_required
def product_model_update_view(request, product_id=None):
    instance = get_object_or_404(ProductModel, id=product_id)
    form = ProductModelForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Producto actualizado con éxito")
        return redirect("detail", product_id=instance.id)
    context = {"form": form}
    template = "layouts/ecommerce/update-view.html"
    return render(request, template, context)

# @login_required
def product_model_create_view(request):
    form = ProductModelForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Producto creado con éxito")
        return redirect("detail", product_id=instance.id)
    context = {"form": form}
    template = "layouts/ecommerce/create-view.html"
    return render(request, template, context)

def product_model_detail_view(request, product_id):
    instance = get_object_or_404(ProductModel, id=product_id)
    context= {"product": instance }
    template = "layouts/ecommerce/detail-view.html"
    return render(request, template, context)
