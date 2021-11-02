from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from cart.cart import Cart
from shop.models import Book
from decimal import Decimal
from .forms import OrderCreateForm
from .models import OrderItem, Order
from django.shortcuts import render, redirect
from .decorators import only_in_process_order, only_if_cart


@login_required(login_url='/accounts/login')
def order_create(request):
    cart = Cart(request).get_cart(request)
    temp_cart = cart.copy()
    books_ids = cart.keys()
    books = Book.objects.filter(id__in=books_ids)
    cart_total_price = 0
    for book in books:
        cart_item = temp_cart[str(book.id)]
        cart_item['book'] = book
        cart_item['total_price'] = (Decimal(cart_item['price']) * cart_item['quantity'])
        cart_total_price += sum(Decimal(item['price']) * item['quantity'] for item in temp_cart.values())

    if request.method == "GET":
        form = OrderCreateForm
        return render(request, 'orders/order_create.html', {'order_form': form})

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(address=request.POST['address'],
                                         user=request.user,
                                         first_name=request.POST['first_name'],
                                         last_name=request.POST['last_name'],
                                         email=request.POST['email'],
                                         postal_code=request.POST['postal_code'],
                                         city=request.POST['city'])

            for book in books:
                cart_item = temp_cart[str(book.id)]
                OrderItem.objects.create(order=order,
                                         book=book,
                                         price=cart_item['total_price'],
                                         quantity=cart_item['quantity'])
        else:
            return HttpResponse('неверно заполнена форма')

        Cart.clear(request)
        return redirect('orders:in_process_order')


@login_required(login_url='/accounts/login')
def in_process_order(request):
    orders = request.user.order_user.filter(paid=False)
    if request.method == "POST" and 'btn_pay' in request.POST:
        order = Order.objects.get(id=request.POST['btn_pay'])
        order.paid = True
        order.save()
        return redirect('/orders/order_history')
    if request.method == "POST" and 'btn_see':
        return redirect('/orders/order_history')
    return render(request, 'orders/in_process_order.html', {'orders': orders})


@login_required(login_url='/accounts/login')
def order_history(request):
    orders = request.user.order_user.filter(paid=True)

    return render(request, 'orders/order_history.html', {'orders': orders})
