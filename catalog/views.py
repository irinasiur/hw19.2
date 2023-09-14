from django.forms import inlineformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Category, Version


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        if not self.request.user.is_anonymous:
            return Product.objects.filter(user=self.request.user)
        return Product.objects.all()


# def index(request):
#     product_list = Product.objects.all()
#     context = {
#         'object_list': product_list,
#         'title': 'Продукты',
#         'text': 'Всегда самые свежие, натуральные, выращенные в экологически чистых уголках природы специально для вас'
#     }
#     return render(request, 'catalog/product_list.html', context)

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


class CategoriesDetailView(DetailView):
    model = Category
    template_name = 'catalog/product_detail.html'


# def product(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#
#     context = {
#         'product': product,
#         'title': 'ДЛЯ ВАС',
#         'text': 'Всегда самые свежие, натуральные, выращенные в экологически чистых уголках природы специально для вас'
#
#     }
#     return render(request, 'catalog/product_detail.html', context)


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


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()

        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    success_url = reverse_lazy('catalog:index')

    # def get_success_url(self):
    #     return reverse('catalog:product_update', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)
        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index')

class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm


class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm


class VersionListView(ListView):
    model = Version


class VersionDetailView(DetailView):
    model = Version


class VersionDeleteView(DeleteView):
    model = Version
    success_url = reverse_lazy('catalog:index')
