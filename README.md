# API для YaTube

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/dptvsh/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### Пример запроса API

Для получения конкретной публикации нужно выполнить запрос, где {id} соответствует id необходимой публикации:

```
GET /api/v1/posts/{id}/
```
В случае успешного выполнения запроса будет получен ответ в формате json:
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```
Более детальная информация по каждому доступному эндпоинту представлена в файле redoc.yaml.
