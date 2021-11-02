from django.contrib import admin
from .models import *
from django.contrib.auth.models import User


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['book']


class OrderAdmin(admin.ModelAdmin):

    list_display = ('id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid', 'created', 'updated', 'completed')
    list_filter = ('paid', 'created', 'updated', 'completed')
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
