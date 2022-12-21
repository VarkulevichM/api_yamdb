# Групповой проект команды под номером 22
api_yamdb
Проект YaMDb собирает отзывы пользователей на произведения и делит их категории:
* Книги
* Фильмы
* Музыка
# Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
### Как запустить проект:
Клонировать репозиторий:
```
git@github.com:VarkulevichM/api_yamdb.git
```
Перейти в каталог с проектом в командной строке:
```
cd api_yambd
```
Создать и активировать виртуальное окружение:
(для Windows везде использовать python а не python3)
```
python3 -m venv env 
```
```
source env/bin/activate
```
Обносить pip и установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip 
```
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```
```
Для того, чтобы заполнить базу, нужно прпоисать данные команды
запускать надо в таком порядке из директории где находится manage.py

python manage.py importCSVUsers
python manage.py importCSVCategory
python manage.py importCSVGenre
python manage.py importCSVTitels
python manage.py importCSVGenereTitle
python manage.py ImportCSVReview
python manage.py importCSVComments
```
### Примеры запросов
Запрос с помощью **POST** метода на страницу: http://127.0.0.1:8000/api/v1/auth/signup/
для регистрации пользователя:

    {
    "email": "user@example.com",
    "username": "string"
    }

Запрос с помощью **POST** метода на страницу: http://127.0.0.1:8000/api/v1/categories/
для добавления новой категории:

    {
    "name": "string",
    "slug": "string"
    }
Полный список запросов API находятся в документации:

http://127.0.0.1:8000/redoc/
### Технологии:
- Python 3.7
- Django 2.2.16
- django rest framework 3.12.4
- Simple JWT 5.2.2

Авторы:
Варкулевич Михаил
Вдовин Данил
Гуржий Борис