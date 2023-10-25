from django.contrib import admin
from .models import MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    """
    Класс для настройки административной панели меню.
    """
    list_display = ['name', 'url', 'parent']
    search_fields = ['name', 'url']

    list_filter = ['parent']
