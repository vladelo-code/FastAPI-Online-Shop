from ecommerce.orders.worker import celery_app
from ecommerce.orders.mail import send_email

@celery_app.task
def send_order_confirmation(to_email: str):
    subject = "Спасибо за заказ!"
    body = """
    <h2>Ваш заказ успешно оформлен</h2>
    <p>Спасибо, что выбрали наш магазин.</p>
    """
    send_email(to_email, subject, body)
