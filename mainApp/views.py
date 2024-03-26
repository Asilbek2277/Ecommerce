from django.shortcuts import render

from django.views import View
from .models import *

class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'home.html')
        return render(request, 'home-unauth.html')


class Categories(View):
    def get(self, request):
        context={
            'categories': Category.objects.all(),
            'subcategories': Subcategory.objects.all()
        }
        return render(request, 'categories.html', context)


class SubCategories(View):
    def get(self, request, pk):
        context = {
            'subcategories': Subcategory.objects.filter(category__id=pk)
        }
        return render(request, 'subCategories.html', context)


class ProductsView(View):
    def get(self, request):
        return render(request, 'products.html')

class ProductView(View):
    def get(self, request):
        return render(request, 'product.html')



