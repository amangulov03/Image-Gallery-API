# Image Gallery API (Django + Cloudinary)

## Описание проекта
REST API для загрузки, хранения и удаления изображений с использованием **Django REST Framework** и облачного хранилища **Cloudinary**.

API позволяет:
- Загрузить изображение в облако Cloudinary;
- Получить список всех изображений;
- Посмотреть подробную информацию об одном изображении;
- Удалить изображение как из базы, так и из облака.


## Используемые технологии
- **Python**
- **Django**
- **Django REST Framework**
- **Cloudinary**


## Установка и запуск

### 1 Клонируйте репозиторий
```bash
git clone https://github.com/amangulov03/Image-Gallery-API.git
cd Image-Gallery-API
```

### 2 Создайте и активируйте виртуальное окружение

```bash
python -m venv venv
. venv/bin/activate       # Linux/Mac
venv\Scripts\activate          # Windows
```

### 3 Создайте файл `requirements.txt` в корне вашего проекта (рядом с `manage.py`) и добавьте в него следующие зависимости на основе вашего кода

```bash
djangorestframework
cloudinary
pillow
python-decouple
psycopg2-binary
```
*Чтобы установить зависимости из файла `requirements.txt`, выполните следующую команду в терминале в корне проекта:*

```bash
pip install -r requirements.txt
```

*Если файла `requirements.txt` нет — установите пакеты вручную:*

```bash
pip install djangorestframework cloudinary pillow psycopg2-binary python-decouple
```


### 4 Настройка Cloudinary

Создайте аккаунт на [https://cloudinary.com](https://cloudinary.com)
и получите данные для подключения:

* **CLOUD_NAME**
* **API_KEY**
* **API_SECRET**

Добавьте их в `settings.py`:

```bash
cloudinary.config(
    cloud_name = 'ваше имя в облаке',
    api_key = 'ваш api key',
    api_secret = config('API_SECRET')
    secure=True
)
```

### 5 Создайте файл .env в корне вашего проекта (рядом с manage.py) и добавьте в него следующие строки с указанными значениями

```bash
SECRET_KEY=ваш-секретный-ключ

DB_NAME=ваше имя в базе данных
DB_USER=ваш-пользователь-базы данных
DB_PASSWORD=ваш пароль к базе данных
DB_HOST=localhost
DB_PORT=5432

API_SECRET=ваш-api-секрет от Cloudinary
```

### 6 Миграции и запуск проекта

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

После запуска сервер будет доступен по адресу:
**[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**


## API Эндпоинты

| Метод    | URL                 | Описание                                 |
| -------- | ------------------- | ---------------------------------------- |
| `POST`   | `/api/images/`      | Загрузка изображения                     |
| `GET`    | `/api/images/`      | Получить список изображений              |
| `GET`    | `/api/images/<id>/` | Получить информацию об одном изображении |
| `DELETE` | `/api/images/<id>/` | Удалить изображение                      |


## Примеры curl-запросов

### 1 Загрузка изображения

```bash
curl -X POST http://127.0.0.1:8000/api/images/ \
  -F "title=Мой фото" \
  -F "description=Фото на улице" \
  -F "file=@/путь/к/твоему/my_photo.jpg"
```

### 2 Получение списка изображений

```bash
curl -X GET http://127.0.0.1:8000/api/images/
```

### 3 Получение информации об одном изображении

```bash
curl -X GET http://127.0.0.1:8000/api/images/1/
```

### 4 Удаление изображения

```bash
curl -X DELETE http://127.0.0.1:8000/api/images/1/
```


## Структура проекта

```
image_gallery_project/
│
├── images/
│   ├── models.py          # Модель ImageItem
│   ├── serializers.py     # Сериализатор
│   ├── views.py           # ViewSet с create() и destroy()
│   ├── services.py        # Функция upload_to_cloudinary()
│   ├── urls.py            # Маршрутизация API
│
├── core/
│   ├── settings.py        # Настройки проекта и Cloudinary
│   ├── urls.py            # Главная маршрутизация API
│
├── requirements.txt       # Зависимости проекта
└── manage.py
```

## Автор

**Эмир Амангулов**
Python/Django Developer — стажёр

