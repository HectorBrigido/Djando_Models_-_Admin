from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView, RedirectView

from products.views import (
    ProductListView,
    ProductDetailView,
    DigitalProductListView, 
    ProductIDRedirectView, 
    ProductRedirectView,
    ProtectedProductDetailView,
    ProtectedProductCreateView,
    ProtectedProductUpdateView,
    ProtectedProductDeleteView,
)

urlpatterns = [
    path("about-us/", RedirectView.as_view(pattern_name="products:about", permanent=True)),
    path("about/", TemplateView.as_view(template_name="products/about.html"), name="about"),
    path("team/", TemplateView.as_view(template_name="products/team.html"), name="team"),
    path("products/", ProductListView.as_view()),
    path("digital-products/", DigitalProductListView.as_view()),
    path("products/<int:pk>/", ProductDetailView.as_view()),
    path("products/<slug:slug>/", ProductDetailView.as_view()),
    path("p/<int:pk>/", ProductIDRedirectView.as_view()),
    path("p/<slug:slug>/", ProductRedirectView.as_view()),

    path("my-products/create/", ProtectedProductCreateView.as_view()),
    # path("my-products/<slug:slug>/", ProtectedProductDetailView.as_view()),
    path("my-products/<slug:slug>/", ProtectedProductUpdateView.as_view()),    
    path("my-products/<slug:slug>/delete/", ProtectedProductDeleteView.as_view()), 
]