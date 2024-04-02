from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.apps import apps


@receiver(post_migrate)
def create_default_menu_items(sender, **kwargs):
    if apps.ready:
        from menu.models import MenuItem
        if MenuItem.objects.count() == 0:
            # Создаем объекты MenuItem только если в базе данных нет ни одной записи
            MenuItem.objects.create(
                title='Новый пункт меню', url='/новая-страница/')
