from django.db import models


class MenuItem(models.Model):
    """
    Модель для хранения элементов меню.
    """
    name = models.CharField(max_length=100, help_text="Название элемента меню")
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children',
                               help_text="Родительский элемент меню (пусто для корневых элементов)")
    url = models.CharField(max_length=100, help_text="URL элемента меню")

    def __str__(self):
        return self.name
