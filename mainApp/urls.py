from django.urls import path
from mainApp.views import *

urlpatterns=[
    path('categories/', Categories.as_view(), name='category'),
    path('subcategories/<int:pk>/', SubCategories.as_view(), name='SubCategories'),
    path('products/', ProductsView.as_view(), name='products'),
    path('product/', ProductView.as_view(), name='product'),
]



