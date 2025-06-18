![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-009688?logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-336791?logo=postgresql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red?logo=sqlalchemy)
![Alembic](https://img.shields.io/badge/Alembic-Migrations-8A2BE2)
![Pydantic](https://img.shields.io/badge/Pydantic-Validation-3776AB)
![Celery](https://img.shields.io/badge/Celery-TaskQueue-37814A?logo=celery)
![Redis](https://img.shields.io/badge/Redis-Broker-DC382D?logo=redis)
![Pytest](https://img.shields.io/badge/Pytest-Testing-0A9EDC?logo=pytest)
![Docker](https://img.shields.io/badge/Docker-Container-2496ED?logo=docker)
![HTTPX](https://img.shields.io/badge/httpx-AsyncClient-blueviolet)
![Passlib](https://img.shields.io/badge/Passlib-Bcrypt-FF6F61)
![OAuth2](https://img.shields.io/badge/Auth-OAuth2-blue)
![JWT](https://img.shields.io/badge/JWT-Token-000000?logo=jsonwebtokens)
![SMTP](https://img.shields.io/badge/SMTP-YandexMail-yellow)

# 🛍️ FastAPI Online Shop

FastAPI Online Shop — это полнофункциональное e-commerce API-приложение, построенное с использованием FastAPI, SQLAlchemy, PostgreSQL и Celery с Redis.

![Technology stack](docs/screenshots/technology-stack.png)

## 🚀 Возможности

- 📦 Управление продуктами и категориями
- 🛒 Добавление и удаление товаров из корзины
- 🧾 Оформление заказов
- ✅ Аутентификация через JWT
- 📧 Уведомление по email при оформлении заказа
- 🧵 Асинхронные задачи через Celery и Redis
- 🧪 Unit тесты с использованием Pytest и httpx

## 📸 Примеры работы

### 🔐 Аутентификация
![Login screen](docs/screenshots/login.png)

### 🔍 Общий вид
![Overview](docs/screenshots/overview-1.png)
![Overview](docs/screenshots/overview-2.png)

### 📦 Создание товара
![Create product](docs/screenshots/create-product-1.png)
![Create product](docs/screenshots/create-product-2.png)

## 🧰 Технологический стек

- **Язык:** Python 3.11+
- **Фреймворк:** FastAPI
- **Асинхронность:** asyncio, httpx
- **База данных:** PostgreSQL (через SQLAlchemy ORM)
- **Миграции базы данных:** Alembic
- **Схемы данных и валидация:** Pydantic v2
- **Аутентификация:** OAuth2, JWT
- **Хеширование паролей:** Passlib + Bcrypt
- **Очереди фоновых задач:** Celery + Redis
- **Тестирование:** Pytest + pytest-asyncio
- **Работа с email:** SMTP (используется Yandex)
- **Документация:** OpenAPI (автоматически через Swagger UI)


## 📂 Структура проекта

```
ecommerce/
│
├── auth/             # JWT и аутентификация
├── cart/             # Модель и логика корзины
├── orders/           # Обработка заказов + Celery
├── products/         # Категории и продукты
├── user/             # Модели и регистрация пользователя
├── db.py             # Подключение к базе данных
├── config.py         # Конфигурации проекта
│
├── tests/            # Автоматические тесты
│
└── main.py           # Точка входа FastAPI
```

## ⚙️ Установка и запуск

```bash
# 1. Клонируй репозиторий
git clone https://github.com/vladelo777/FastAPI-Online-Shop.git
cd FastAPI-Online-Shop

# 2. Создай виртуальное окружение
python -m venv .venv
source .venv/bin/activate

# 3. Установи зависимости
pip install -r requirements.txt

# 4. Настрой переменные окружения
cp .env.template .env

# 5. Примените миграции Alembic
alembic upgrade head

# 6. Запуск сервера FastAPI
uvicorn main:app --reload

# 7. Запуск Redis (если не запущен)
brew services start redis  # macOS
# redis-server             # Linux/WSL

# 8. Запуск Celery
celery -A ecommerce.orders.worker.celery_app worker --loglevel=info

## 🧪 Запуск тестов

```bash
pytest
```

## ⚙️ Переменные окружения

Файл `.env.template` для всех необходимых переменных.


## 📬 **Контакты**

Автор: Владислав Лахтионов  
GitHub: [vladelo777](https://github.com/vladelo777)  
Telegram: [@vladelo](https://t.me/vladelo)  

💌 Не забудьте поставить звезду ⭐ на GitHub, если вам понравился проект! 😉
