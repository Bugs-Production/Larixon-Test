from django.contrib import admin
from .models import Category, City, Advert


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'category', 'views',)
    search_fields = ('title', 'city__name', 'category__name',)
    list_filter = ('city', 'category',)
    readonly_fields = ('views',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    search_fields = ('name',)
