from django.contrib import admin

from shop.models import Category, Product, Order, Review

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name', )}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'available', 'created_at')
    list_filter = ('available', 'category')
    list_editable = ('price', 'stock', 'available')
    prepopulated_fields = {'slug': ('name', )}

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'address', 'created_at', 'total_cost', 'paid')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'text', 'rating')