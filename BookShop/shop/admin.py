from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'image_show', 'pub_year', 'price',
                    'language', 'num_pages', 'availability', 'get_category', 'get_author', )
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('category', 'availability')
    list_editable = ('price', 'availability')

    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60'/".format(obj.image.url))
        return "None"

    image_show.__name__ = 'изображение'


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(UserBookRate)
class RateAdmin(admin.ModelAdmin):
    list_display = ('user', 'rate', 'book')
