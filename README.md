# Тестовое задание

Данный репозиторий представляет собой решение тестового задания изложенного в [TODO.md](TODO.md)

### Описание проекта

В качестве задание выполнено возможное API для книжной библиотеки, написанное с использованием **Django REST Framework**
.

В проекте имеется одно приложения bookstore, две модели описывающего автора и книги данного автора со связью один ко
многим. Сериализаторы, Вьюсеты необходимые для обмена данными при запросах с клиента.

Ко всем спискам моделей применяется индивидуальная пагинация. Для различных вьюсетов доступна специфичная фильтрация
внедренная с использованием библиотеки **django-filters**

Используется авторизация по токену с разграничением прав доступа.

### Установка

Для корректной работы требуется Python 3.9.
После загрузки все файлов репозитория необходимо установить все необходимые библиотеки перечисленные в
файле [requirements.txt](requirements.txt) в виртуальное окружение выполнив команду из папки 
репозитория:

`pip3 install -r requirements.txt`

В проекте имеются тестовые данные для цели демонстрации. Для их использования необходимо из папки backend выполнить 
команду:

`python3 manage.py filldb`

Для получения информации о пользователях, группах и правах доступа создаваемых, при наполнении базы данных обратитесь к
данному [файлу](backend/bookstore/management/commands/filldb.py)

### Методы API. Примеры

#### Авторизация

Метод: POST  
Ендпоинт: http://127.0.0.1:8000/api/auth/  
Тело запроса:

```json
{
  "username": "staff",
  "password": "staff"
}
```

Тело ответа:

```json
{
  "token": "182afc4928d94f215b0d7b8646ebec87d257e004"
}
```

Данный токен необходимо использовать в заголовках для всех последующих методов

```
"Authorization": "Token 182afc4928d94f215b0d7b8646ebec87d257e004"
```

#### Получение списка объектов

В АПИ доступно два GET метода для получения обектов Book и Author с соответствующими ендпоинтами:  
http://127.0.0.1:8000/api/books/  
http://127.0.0.1:8000/api/authors/

Для каждого из метода доступны параметры offset (по умолчанию 5 для books и 3 для authors) и limit с помощью которых
можно управлять пагинацией с клиента.

К каждому из методов добавлены индивидуальные параметры для обеспечения возможности фильтрации исходя из **содержимого**
фильтра.

Параметры для фильтрации по списку Book:

* author__first_name - для фильтрации книг по имени автора
* author__last_name - для фильтрации книг по фамилии автора
* name - для фильтрации по названию книги
* published_year_gte - для указания нижней границы года публикации книги
* published_year_lte - для указания верхней границы года публикации книги

Параметры для фильтрации по списку Author:

* first_name - для фильтрации книг по имени автора
* last_name - для фильтрации книг по фамилии автора
* birthdate_gte - для указания нижней границы даты рождения автора
* birthdate_lte - для указания верхней границы даты рождения автора

Пример ответа при получении списка книг:

```json lines
{
  "count": 17,
  "next": "http://127.0.0.1:8000/api/books/?limit=5&offset=5",
  "previous": null,
  "results": [
    {
      "id": 10,
      "name": "1984",
      "publishedYear": 1949,
      "cover": "http://127.0.0.1:8000/media/books_cover/1984.jpeg",
      "author": 5
    },
    {
      "id": 5,
      "name": "Американская трагедия",
      "publishedYear": 1925,
      "cover": "http://127.0.0.1:8000/media/books_cover/american_tragedy.jpeg",
      "author": 2
    }
  ]
}
```

#### Получение деталей по объекту

Метод: GET  
Ендпоинт: http://127.0.0.1:8000/api/books/ *pk*  
где pk - id Книги.  
Соответсвующий эндпоинт используется для получения информации по автору:
http://127.0.0.1:8000/api/authors/ *pk*   
где pk - id Автора

Пример:

GET запрос: http://127.0.0.1:8000/api/books/5/  
тело ответа:

```json lines
{
  "id": 5,
  "name": "Американская трагедия",
  "publishedYear": 1925,
  "cover": "http://127.0.0.1:8000/media/books_cover/american_tragedy.jpeg",
  "author": 2
}
```

#### Изменение объекта

Изменение объекта осуществляется по аналогичному ендпоинту что и для просмотра детальной информации по нему с методом
PUT и указанием всех полей по объекту в теле запроса (включая неизменяемые)

#### Удаление объекта

Удаление объекта осуществляется по аналогичному ендпоинту что и для просмотра детальной информации по нему с методом
DELETE.

### Проверка задания

В проекте используется авторизация по токену, и для проверки работы методов
присутсвуют заранее подготовленные скрипты в папке [pyclient](pyclient) написанные
с использованием библиотеки requests. 

Однако можно проверить работособность методов API и ограничение прав доступа
с помощью стандартного рендерера Django REST Framework апи в браузере.
Для этого в файле [settings.py](backend/backend/settings.py) необходимо отключить 
авторизацию по токену и подключить сессионную авторизацию:

```python
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication'
    ]
```

Данное изменение позволит авторизовываться браузерного интерфейса постовляемого с фреймворком.
