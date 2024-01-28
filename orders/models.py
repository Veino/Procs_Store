from django.db import models
from users.models import ProcsUser
from products.models import Product
# Create your models here.

class Shipping_Address(models.Model):
    address = models.CharField(max_length=300, blank=True)
    user=models.ForeignKey(ProcsUser, default=1, on_delete=models.CASCADE)
    postal_code = models.CharField(max_length=7, blank=True)
    person = models.CharField(max_length=50, blank=True)
    contact = models.CharField(max_length=11, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f'{self.person} shipping address'

OrderStatus= [
    ('pending', 'Pending'),
    ('cancelled', 'Cancelled'),
    ('complete', 'Complete'),
    
]



class Order(models.Model):
    buyer = models.ForeignKey(ProcsUser, on_delete=models.CASCADE)
    shipping_address = models.ForeignKey(Shipping_Address, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=20, choices=OrderStatus, default='Pending')
    
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f'{self.buyer.get_full_name()} Order'
    

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, related_name="OrderItems", on_delete=models.CASCADE)
    quantity = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",  )

    def __str__(self):
        return f'{self.order.buyer.get_full_name()} Order Item'