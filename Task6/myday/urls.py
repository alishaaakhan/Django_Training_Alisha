from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("newproductform/", newProductForm, name="newproductform"),
    path("createproduct/", createproduct, name="create"),
    path("productlist/", productlist, name="read"),
    path("updateproductform/", updateProductForm, name="updateproductform"),
    path("updateProduct/", updateProduct, name="update"),
    path("deleteProduct/", deleteProduct, name="delete"),
]

