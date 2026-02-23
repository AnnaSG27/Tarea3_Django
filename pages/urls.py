from django.urls import path
from .views import ProductCreateView, ProductIndexView, ProductShowView, ProductListView
from django.http import HttpResponse


urlpatterns = [
    path('products/', ProductIndexView.as_view(), name='products'),
    path('products/<int:id>/', ProductShowView.as_view(), name='product-show'),
    path('products-list/', ProductListView.as_view(), name='products-list'),
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/created/', 
     lambda request: HttpResponse("Product successfully created"), 
     name='product-created'),
]
