# Cat API 

Это приложение для работы с API по учету котов и их пород. Оно построено на Django, использует Django REST Framework для создания API и JWT для аутентификации.

## Функциональность

- CRUD-операции для котов и пород.
- JWT-аутентификация для создания, редактирования и удаления котов.
- Фильтрация котов по породам.
- Документация API через Swagger и ReDoc.

## Требования

- Python 3.8+
- Django 3.2+
- Django REST Framework
- Django SimpleJWT
- Django Filters
- drf-spectacular

## Установка

1. **Установите зависимости:** 
    
        - pip install -r requirements.txt

2. **Примените миграции для настройки базы данных:**

        - python manage.py makemigrations
     
        - python manage.py migrate

3. **Создайте суперпользователя для доступа в админ-панель:**

        - python manage.py createsuperuser

4. **Запустите сервер разработки:**

        - python manage.py runserver

## Административный интерфейс 

* Доступ к сайту администратора находится по адресу  http://127.0.0.1:8000/admin/. Войдите, используя данные учетной записи суперпользователя, созданные ранее.
* Здесь вы можете добавлять, редактировать и удалять данные.

## API Endpoints

**JWT-аутентификация:**

- POST /api/v1/token/: Получение токена.
- POST /api/v1/token/refresh/: Обновление токена.

**Коты (Cats):**

- GET /api/v1/cats/: Получение списка котов.
- POST /api/v1/cats/: Создание кота (требуется аутентификация).
- GET /api/v1/cats/{id}/: Получение информации о конкретном коте.
- PUT /api/v1/cats/{id}/: Полное обновление информации о коте (требуется аутентификация).
- DELETE /api/v1/cats/{id}/: Удаление кота (требуется аутентификация).

**Породы (Breeds):**

- GET /api/v1/breeds/: Получение списка пород.
- POST /api/v1/breeds/: Создание породы (требуется аутентификация).


**Фильтрация котов по породе:**

- GET /api/v1/cats/?breed=<id>: Получение котов, относящихся к конкретной породе.