from django.db import models

# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=255)
    category_description=models.TextField()

class Product(models.Model):
    product_name=models.CharField(max_length=200)
    product_description=models.TextField()
    product_category=models.ForeignKey(Category, on_delete=models.CASCADE)
    product_price=models.DecimalField(max_digits=10,decimal_places=2)
    product_stock=models.IntegerField()
    product_image=models.ImageField(upload_to='media/',null=True,blank=True)
    product_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name
    


    


