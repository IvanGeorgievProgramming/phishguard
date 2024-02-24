from flask import current_app
import smtplib

from app.services.email_management.compose_email_message import compose_email_message

def send_email(email_receiver, data):
    email_sender = current_app.config["EMAIL_SENDER"]
    email_password = current_app.config["EMAIL_PASSWORD"]
    smtp_ssl_port = current_app.config["SMTP_SSL_PORT"]
    
    try:
        msg = compose_email_message(email_sender, email_receiver, data)

        with smtplib.SMTP_SSL("smtp.gmail.com", smtp_ssl_port) as smtp:
            smtp.login(email_sender, email_password)
            smtp.send_message(msg)
    except Exception as e:
        print("Error sending email: " + str(e))
