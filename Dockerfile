FROM python:3.11-slim

# Системные зависимости для компиляции и PostgreSQL клиента
RUN apt-get update && apt-get install -y build-essential libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# Рабочая директория
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем всё приложение в контейнер
COPY . .

# Открываем порт 8000
EXPOSE 8000

# Команда запуска uvicorn при старте контейнера
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]