from django.urls import path
from . import views

urlpatterns = [
    path('api/create-address/', views.createAddress, name="createAddress"),
    path('api/edit-address/<str:aid>/', views.updateAddress, name="editAddress"),
    path('api/delete-address/<str:aid>/', views.delAddress, name="deleteAddress"),
]