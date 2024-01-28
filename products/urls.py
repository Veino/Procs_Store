from django.urls import path
from . import views

urlpatterns = [
    path("api/product/<str:pid>/", views.singleProduct, name="ProductView"),
    path("api/products/", views.Products, name="products"),
]