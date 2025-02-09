from django.db import models

# Create your models here.

class Category(models.Model):
    CATEGORY_CHOICES=[
        ("men","men"),
        ("women","women")
    ]

    category_name=models.CharField(max_length=255, choices=CATEGORY_CHOICES, unique=True)
    category_description=models.TextField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.category_name
    

class Product(models.Model):
    product_name=models.CharField(max_length=200)
    product_description=models.TextField()
    product_category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    product_image=models.ImageField(upload_to='media/',null=True,blank=True)
    product_price=models.DecimalField(max_digits=10,decimal_places=2)
    brand=models.CharField(max_length=200)
    product_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name
    

class ProductVariant(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name="variants")
    variant_name=models.CharField(max_length=200)
    variant_price=models.DecimalField(max_digits=10,decimal_places=2)
    variant_stock=models.IntegerField()
    variant_color=models.CharField(max_length=200)
    variant_size=models.CharField(max_length=200)


    def __str__(self):
        return self.variant_name