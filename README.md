# Меню на Django

Проект Django для создания древовидного меню с использованием кастомных тегов.

## Установка

1. Клонируйте репозиторий на вашем локальном компьютере:

   ```bash
   git clone https://github.com/AndreyAgeew/mymenu.git
   
2. Перейдите в каталог проекта:

   ```bash
   cd mymenu

3. Создайте и активируйте виртуальное окружение:

   ```bash
   python -m venv venv
   source venv/bin/activate  # На Windows используйте venv\Scripts\activate

4. Установите зависимости::

   ```bash
   pip install -r requirements.txt

5. Выполните миграции для создания базы данных:

   ```bash
   python manage.py migrate
   
6. Создайте суперпользователя для доступа к админке:

   ```bash
   python manage.py createsuperuser

7. Запустите сервер разработки Django:

   ```bash
   python manage.py runserver

8. Перейдите в административную панель по адресу http://127.0.0.1:8000/admin/, войдите с учетной записью суперпользователя и добавьте элементы меню в разделе "Menu Items".

9. Теперь вы можете создать страницу, на которой хотите отобразить меню, и использовать кастомный тег {% draw_menu 'main_menu' %} для отображения меню.

## Использование

1. Создайте страницу, на которой хотите отобразить меню.

2. Вставьте тег в ваш HTML-шаблон:

  ```bash
  {% load menu_tags %}
  <div class="menu">
      {% draw_menu 'main_menu' %}
  </div>
   
