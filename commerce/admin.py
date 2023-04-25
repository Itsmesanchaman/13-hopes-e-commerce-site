from django.contrib import admin
from .models import Category,products
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['id','categoryname']
 
@admin.register(products)
class productsAdmin(admin.ModelAdmin):
    list_display = ['id','productname','productdesc','price','Quantity','unit','productimage']

