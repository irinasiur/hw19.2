from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView

from catalog.models import Product, Category


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'


# def index(request):
#     product_list = Product.objects.all()
#     context = {
#         'object_list': product_list,
#         'title': 'Продукты',
#         'text': 'Всегда самые свежие, натуральные, выращенные в экологически чистых уголках природы специально для вас'
#     }
#     return render(request, 'catalog/index.html', context)

class CategoriesListView(ListView):
    model = Category
    template_name = 'catalog/categories.html'
# def categories(request):
#     categories_list = Category.objects.all()
#     context = {
#         'object_list': categories_list,
#         'title': 'Категории',
#         'text': 'Всегда самые свежие, натуральные, выращенные в экологически чистых уголках природы специально для вас'
#     }
#     return render(request, 'catalog/categories.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'


class CategoriesDetailView(DetailView):
    model = Category
    template_name = 'catalog/product.html'


# def product(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#
#     context = {
#         'product': product,
#         'title': 'ДЛЯ ВАС',
#         'text': 'Всегда самые свежие, натуральные, выращенные в экологически чистых уголках природы специально для вас'
#
#     }
#     return render(request, 'catalog/product.html', context)


def contacts(request):
    context = {
        'title': 'Контакты'
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"{name}, {phone},{message}")

    return render(request, 'catalog/contacts.html', context)
