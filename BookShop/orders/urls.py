from django.urls import path
from .views import *

app_name = 'orders'

urlpatterns = [
    path('create/', order_create, name='order_create'),
    path('in_process_order/', in_process_order, name='in_process_order'),
    path('order_history/', order_history, name='order_history')
]
