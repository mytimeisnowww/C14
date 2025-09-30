import os
import smtplib
from email.mime.text import MIMEText


def send_email(recipient_email, subject, body):
    sender_email = os.environ.get("SENDER_EMAIL")
    sender_password = os.environ.get("SENDER_EMAIL_PASSWORD")

    if not sender_email or not sender_password:
        print("Erro: Variáveis de ambiente SENDER_EMAIL ou SENDER_EMAIL_PASSWORD não configuradas.")
        return False

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = recipient_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)
        print(f"E-mail enviado para {recipient_email} com sucesso!")
        return True
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
        return False


if __name__ == "__main__":
    recipient = os.environ.get("EMAIL_RECIPIENT")
    pipeline_status = os.environ.get("PIPELINE_STATUS", "UNKNOWN")
    if recipient:
        send_email(recipient, "Status do Pipeline GitHub Actions",
                   f"Pipeline executado! Status: {pipeline_status}")
    else:
        print("Variável de ambiente EMAIL_RECIPIENT não configurada.")
