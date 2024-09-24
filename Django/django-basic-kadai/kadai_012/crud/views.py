from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Product
from django.urls import reverse_lazy

class TopView(TemplateView):
     template_name = "top.html"  # template_name  Templateファイルをtemplateフォルダからの相対パスで指定

class ProductListView(ListView):
     model = Product  # model　対象のModelクラスを指定する
     paginate_by = 3
     
class ProductCreateView(CreateView):
     model = Product
     fields = '__all__'  # fields　新規作成時にユーザが入力するフィールドを指定する　※ここでは、全フィールドを指定する

class ProductUpdateView(UpdateView):
     model = Product  
     fields = '__all__'
     template_name_suffix = '_update_form'  # デフォルトのTemplateファイル名が新規作成フォームと同じ「pruduct_form.html」になるため、編集用のファイル名を指定する。
     
class ProductDeleteView(DeleteView):
     model = Product
     success_url = reverse_lazy('list')  # 削除成功後に遷移するURL   

class ProductDetailView(DetailView):
    model = Product