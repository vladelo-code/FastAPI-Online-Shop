import smtplib
from email.mime.text import MIMEText
from ecommerce import config


def send_email(to_email: str, subject: str, html_body: str) -> None:
    """
    Отправляет HTML-письмо на указанный email через SMTP сервер.

    Использует настройки SMTP из config для подключения к серверу.

    :param to_email: Адрес получателя письма.
    :param subject: Тема письма.
    :param html_body: HTML содержимое письма.
    :raises Exception: В случае ошибки при отправке письма выводит ошибку в консоль.
    """
    msg = MIMEText(html_body, "html")
    msg["Subject"] = subject
    msg["From"] = config.SMTP_USER
    msg["To"] = to_email

    try:
        with smtplib.SMTP(config.SMTP_HOST, config.SMTP_PORT) as server:
            server.starttls()
            server.login(config.SMTP_USER, config.SMTP_PASSWORD)
            server.sendmail(config.SMTP_USER, [to_email], msg.as_string())
        print(f"✅ Email was sent to {to_email}")
    except Exception as e:
        print(f"❌ Email sending error: {e}")
