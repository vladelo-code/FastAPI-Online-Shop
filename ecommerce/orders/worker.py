from celery import Celery

from ecommerce import config

celery_app = Celery(
    "ecommerce",
    broker=f"redis://{config.REDIS_HOST}:{config.REDIS_PORT}/{config.REDIS_DB}",
    backend=f"redis://{config.REDIS_HOST}:{config.REDIS_PORT}/{config.REDIS_DB}"
)

celery_app.conf.imports = [
    "ecommerce.orders.tasks",
]
