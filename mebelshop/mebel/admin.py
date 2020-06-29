from django.contrib import admin
from .models import Categories, Materials, Colors, Sizes, Products


class CategoriesConfig(admin.ModelAdmin):
    fields = ('name', 'icon')
    list_display = fields


admin.site.register(Categories, CategoriesConfig)


class MaterialsConfig(admin.ModelAdmin):
    fields = ('name',)
    list_display = fields


admin.site.register(Materials, MaterialsConfig)


class ColorsConfig(admin.ModelAdmin):
    fields = ('name', 'color')
    list_display = fields


admin.site.register(Colors, ColorsConfig)


class SizesConfig(admin.ModelAdmin):
    fields = ('name',)
    list_display = fields


admin.site.register(Sizes, SizesConfig)


class ProductsConfig(admin.ModelAdmin):
    fields = (
        'name',
        'slug',
        'brand',
        ('category', 'availability', 'new'),
        ('price', 'price_discount', 'discount'),
        'materials',
        'colors',
        'sizes',
        'img1',
        'img2',
        'img3',
        'img4',
        'img5'
    )
    list_display = ('name', 'category', 'price')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Products, ProductsConfig)