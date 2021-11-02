from django.urls import path
from .views import *

app_name = 'shop'

urlpatterns = [
    path('searchbar', searchbar, name="search"),
    path('', Catalog.as_view(), name="main"),
    path('<slug:category_slug>', CategoryDetail.as_view(), name="category_detail"),
    path('books/<slug:book_slug>', BookDetail.as_view(), name="book_detail"),
]
