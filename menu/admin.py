from django.contrib import admin
from .models import MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    """
    Класс для настройки административной панели меню.
    """
    list_display = ['name', 'url', 'parent']
    search_fields = ['name', 'url']

    filter_horizontal = ('parent',)  # Используйте filter_horizontal для выбора родительских элементов.
