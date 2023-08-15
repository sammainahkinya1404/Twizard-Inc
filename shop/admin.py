from django.contrib import admin
from .models import Category,Product

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields={'slug': ('name',)}

class ProductAdmin(admin.ModelAdmin):
    list_display=['category','created_by','name','title','description','author','price','created','updated','slug','in_stock','is_active']
    prepopulated_fields={'slug': ('name',)}

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)