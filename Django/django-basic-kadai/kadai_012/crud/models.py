from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
         return self.name

class Product(models.Model):
    name = models.CharField(max_length=200) # name 商品名を文字列型で定義する最大文字列は200
    price = models.PositiveIntegerField() # price 金額を正の整数型で定義する
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # on delete データが削除されると、関連するすべてのデータが削除される
    img = models.ImageField(blank=True, default='noImage.png')  # 商品Modelに画像フィールドを追加する
    text = models.TextField(blank=True,null=True,)  # 商品の詳細説明フィールドを追加する
    
    def __str__(self):
        return self.name
    
    # 新規作成・編集完了時のリダイレクト先
    def get_absolute_url(self):
        return reverse('list')  # reverse = 名前からURLを取得する関数
    
