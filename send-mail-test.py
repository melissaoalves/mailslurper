import smtplib
from email.mime.text import MIMEText

SMTP_SERVER = "localhost"
SMTP_PORT = 2500

FROM_EMAIL = "melissaoalvesmoa@gmail.com"
TO_EMAIL = "melissaalves@ufpi.edu.br"

SUBJECT = "Teste SMTP"
BODY = """
Olá,

Este é email é um teste.

Atenciosamente,
Melissa
"""

def send_email():
    try:
        msg = MIMEText(BODY)
        msg["Subject"] = SUBJECT
        msg["From"] = FROM_EMAIL
        msg["To"] = TO_EMAIL

        print("Conectando ao servidor SMTP...")
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            print("Enviando email...")
            server.sendmail(FROM_EMAIL, [TO_EMAIL], msg.as_string())
        print("Email enviado com sucesso.")

    except Exception as e:
        print("Erro ao enviar o email:", e)

if __name__ == "__main__":
    send_email()
