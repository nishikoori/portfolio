from django.contrib import admin
from .models import Product, Category
from django.utils.safestring import mark_safe

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'image')  # list_display 表示するフィールドを配列で指定する
    search_fields = ('name',)  # search_fields 検索対象のフィールドを配列で指定する
    list_filter = ('category',)  # list_filter　絞り込みフィルターにカテゴリを追加
    
    def image(self, obj):
        return mark_safe('<img src="{}" style="width:100px height:auto;">'.format(obj.img.url))
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # list_display カテゴリのIDと名前を表示する
    search_fields = ('name',)  # search_fields カテゴリ名で検索可能とする
    
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
