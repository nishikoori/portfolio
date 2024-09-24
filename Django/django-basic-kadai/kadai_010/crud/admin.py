from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')  # list_display 表示するフィールドを配列で指定する
    search_fields = ('name',)  # search_fields 検索対象のフィールドを配列で指定する

admin.site.register(Product, ProductAdmin)
