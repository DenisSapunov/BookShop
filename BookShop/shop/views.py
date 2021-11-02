from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import AnonymousUser
from .models import *
from cart.forms import CartAddBookForm
from .forms import RateForm

categories = Category.objects.all()


class Catalog(View):

    def get(self, request):
        books = Book.objects.all()
        return render(request, 'shop/catalog.html', {
            'categories': categories,
            'books': books})


class CategoryDetail(View):

    def get(self, request, category_slug):
        category_detail = Category.objects.get(slug=category_slug)
        books = Book.objects.filter(category=category_detail)
        return render(request, 'shop/category_detail.html', {
            'category_detail': category_detail,
            'categories': categories,
            'books': books})


class BookDetail(View):
    def get(self, request, book_slug):
        book = Book.objects.get(slug=book_slug)
        cart_add_form = CartAddBookForm
        if request.user.is_authenticated:
            rate = UserBookRate.objects.filter(book=book, user=request.user)
        else:
            rate = ''
        return render(request, 'shop/book_detail.html', {
            'categories': categories,
            'book': book,
            'cart_book_form': cart_add_form,
            'rate_form': RateForm,
            'rate': rate
        })

    def post(self, request, book_slug):
        book = Book.objects.get(slug=book_slug)
        form = RateForm(request.POST)
        print(request.POST)
        if request.user.is_authenticated:
            if form.is_valid:
                UserBookRate.objects.create(rate=form.data['rate'], user=request.user, book=book)
            return HttpResponseRedirect(f'/books/{book.slug}')
        else:
            return HttpResponse('Что то пошло не так')


def searchbar(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        books = Book.objects.all().filter(name=search)
        return render(request, "shop/searchbar.html", {'books': books})
