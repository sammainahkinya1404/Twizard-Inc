from django.db import models
from django.contrib.auth.models import User
# Create your modelsfrom 

class Category(models.Model):
    name=models.CharField(max_length=255,db_index=True)
    slug=models.SlugField(max_length=255,unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    category=models.ForeignKey(Category,related_name='product',on_delete=models.CASCADE)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='product_created_by')
    name=models.CharField(max_length=255)
    description=models.TextField(blank=True)
    title=models.CharField(max_length=255)
    image=models.ImageField(upload_to='images/')
    author=models.CharField(max_length=255,default='admin')
    slug=models.SlugField(max_length=255,unique=True)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    in_stock=models.BooleanField(default=True)
    is_active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Products'
        # odering='-created'

    def __str__(self):
        return self.title