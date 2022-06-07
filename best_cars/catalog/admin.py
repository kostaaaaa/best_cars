from django.contrib import admin

from .models import Brand, CarModel


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Brand, BrandAdmin)


class CarModelInline(admin.TabularInline):
    model = CarModel


class CarModelAdmin(admin.ModelAdmin):
    list_display = (
        'brand',
        'model',
        'engine_type',
        'engine_capacity',
        'body_type',
        'power',
        'year',
        'is_available',
    )
    search_fields = ('brand__name', 'model',)
    list_filter = (
        'engine_type',
        'year',
        'body_type',
        'is_available',
    )
    # inlines = [CarModelInline,]


admin.site.register(CarModel, CarModelAdmin)
