from django.contrib import admin

from items.models import Items

# Register your models here.
@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ["name", 'price']