# yatube_api
Социальная сеть блогеров.
В ней можно делать публикации личных дневников, заходить на чужие страницы, подписываться на авторов и комментировать их записи.

### Как запустить проект:
- Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/NColemann/api_final_yatube.git
```
```
cd api_final_yatube
```
- Создать и активировать виртуальное окружение:
```
python3 -m venv venv
```
```
. venv/bin/activate
```
- Установить зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 
- Выполнить миграции:
```
python3 manage.py migrate
```
- В папке с файлом manage.py выполнить команду, для запуска проекта:
```
python3 manage.py runserver
```

### Некоторые примеры запросов к API

#### Cписок всех постов
GET /api/v1/posts/

#### Добавить новый пост
POST /api/v1/posts/
```json
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
#### Получение поста по id
GET /api/v1/posts/{id}/

#### Добавление комментария
POST /api/v1/posts/{post_id}/comments/
```json
{
  "text": "string"
}
```
#### Подписка на пользователя
POST /api/v1/follow/
```json
{
  "following": "username"
}
```
### Технологии
Python 3.10 Django 2.2.18
### Автор
https://github.com/NColemann  

LinkedIn: http://linkedin.com/in/kalimanov
