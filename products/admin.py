from django.contrib import admin

from products.models import CategoryModel, ProductModel
from django.forms import Textarea
from django.db import models


class ProductAdminConfig(admin.ModelAdmin):
    model = ProductModel
    search_fields = ('title', 'price', 'availability', 'date_added')
    list_filter = ('title', 'price', 'availability', 'date_added')
    ordering = ('-date_added',)
    list_display = ('title', 'price', 'availability', 'date_added')
    fieldsets = (
        ('Category', {'fields': ('category',)}),
        ('Product Detail', {'fields': ('title', 'slug', 'descriptions', 'price', 'availability')}),
        ('Image', {'fields': ('image', 'thumbnail')}),
        ('Date Added', {'fields': ('date_added',)}),

    )
    readonly_fields = ['date_added']
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }


admin.site.register(CategoryModel)
admin.site.register(ProductModel, ProductAdminConfig)
