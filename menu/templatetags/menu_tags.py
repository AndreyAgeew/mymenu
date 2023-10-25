from django import template
from menu.models import MenuItem

register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    """
    Кастомный тег для отрисовки меню.

    Args:
        menu_name (str): Название меню.

    Returns:
        str: HTML-код меню.
    """
    menu = MenuItem.objects.get(name=menu_name)

    def render_menu(menu_item):
        """
        Рекурсивная функция для отрисовки меню.

        Args:
            menu_item (MenuItem): Элемент меню.

        Returns:
            str: HTML-код элемента меню и его подменю.
        """
        html = f'<ul><li><a href="{menu_item.url}">{menu_item.name}</a>'
        if menu_item.children.all():
            html += '<ul>'
            for child in menu_item.children.all():
                html += render_menu(child)
            html += '</ul>'
        html += '</li></ul>'
        return html

    return render_menu(menu)
