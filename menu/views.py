from django.shortcuts import render
from .models import MenuItem


def draw_menu(request, menu_name):
    # Получаем все пункты меню по его имени
    menu_items = MenuItem.objects.filter(name=menu_name)

    context = {
        'menu_items': menu_items,
    }

    return render(request, 'menu.html', context)
