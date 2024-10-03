from django.contrib import admin
from .models import *


class RatingInline(admin.TabularInline):
    model = Rating


@admin.register(Cat)


class CatAdmin(admin.ModelAdmin):
    list_display = ('author', 'breed', 'colour', 'age', 'description')
    search_fields = ('colour', 'description')
    list_filter = ('colour', 'age', 'author')
    inlines = [RatingInline]


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    pass






