from django.contrib import admin
from .models import Userprofile, Address, Order, Cart

# Register your models here.
@admin.register(Userprofile)
class UserprofileAdmin(admin.ModelAdmin):
    list_display = ['user', 'profilepic', 'status']
    list_filter = ['user']
    search_fields = ['user']
 
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
	list_display = ['user', 'name', 'email', 'address', 'city', 'state', 'pincode']
	list_filter = ['user']
	search_fields = ['user']
 
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ['user', 'address', 'product', 'quantity', 'totalprice', 'tid', 'tdate', 'payment_status', 'order_status', 'payment_mode']
	list_filter = ['user']
	search_fields = ['user']
 
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
	list_display = ['user', 'product', 'quantity']
	list_filter = ['user']
	search_fields = ['user']