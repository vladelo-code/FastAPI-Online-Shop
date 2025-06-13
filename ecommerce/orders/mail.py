import smtplib
from email.mime.text import MIMEText
from ecommerce import config


def send_email(to_email: str, subject: str, html_body: str):
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
