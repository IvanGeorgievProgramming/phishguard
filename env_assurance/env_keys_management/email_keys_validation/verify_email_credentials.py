import smtplib

def verify_email_credentials(email, password):
    smtp_ssl_port = 465

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", smtp_ssl_port) as smtp:
            smtp.login(email, password)
        return True
    except smtplib.SMTPAuthenticationError:
        return False
