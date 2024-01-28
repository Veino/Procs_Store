from django.urls import path
from . import views

urlpatterns = [
    path("api/products/add/", views.addProduct, name="AddProduct"),
    path("api/products/<str:pid>/", views.singleProduct, name="Product"),
    path("api/products/all/", views.Products, name="AllProducts"),
    path("api/orders/all", views.Orders, name="AllOrders"),
    path("api/orders/<str:oid>/", views.singleOrder, name="Order"),
]