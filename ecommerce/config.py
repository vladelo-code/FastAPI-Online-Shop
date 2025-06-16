from dotenv import load_dotenv
import os

load_dotenv()

# DB PostgreSQL
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_NAME = os.getenv('DATABASE_NAME')

# Test DB PostgreSQL
TEST_DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
TEST_DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
TEST_DATABASE_HOST = os.getenv('DATABASE_HOST')
TEST_DATABASE_NAME = os.getenv('DATABASE_NAME')

# Redis (для Celery)
REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = int(os.getenv('REDIS_PORT'))
REDIS_DB = int(os.getenv('REDIS_DB'))

# SMTP Yandex
SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

# JWT Authentication
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
