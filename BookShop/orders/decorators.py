from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect


def only_if_cart(view_func):
    def wrapper_func(request, *args, **kwargs):
        cart_order = request.session.get(settings.CART_SESSION_ID)
        if cart_order:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse('у вас нет ничего в корзине, чтобы офрмить заказ')

    return wrapper_func


def only_in_process_order(view_func):
    def wrapper_func(request, *args, **kwargs):
        if hasattr(request.user, 'order_user'):
            if not request.user.order_user:
                return redirect('orders:in_process_order')
            else:
                return view_func(request, *args, **kwargs)
        else:
            return redirect('/')

    return wrapper_func
