from django.db import models
from users.models import ProcsUser
# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    user=models.ForeignKey(ProcsUser, default=1, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images', blank=True)
    isCover = models.BooleanField(default=False)