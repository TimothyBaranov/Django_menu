from django.contrib import admin
from .models import MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'parent')
    list_filter = ('parent',)
    search_fields = ('name', 'url')
