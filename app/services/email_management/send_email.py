from flask import current_app
import smtplib

from app.services.email_management.compose_email_message import compose_email_message

def send_email(email_receiver, data):
    """
    Summary: 
        Sends an email containing the analysis results to the user.

    Description: 
        The email sender and password are extracted from the configuration.\n
        The message object is composed using the compose_email_message function.\n
        The SMTP server is created.\n
        The email sender is authenticated.\n
        The email is sent.\n

    Arguments: 
        email_receiver (str): The email address of the receiver.
        data (dict): The data dictionary containing the analysis results.

    Returns: 
        None: The function doesn't return anything.

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console.
    """
    try:
        email_sender = current_app.config["EMAIL_SENDER"]
        email_password = current_app.config["EMAIL_PASSWORD"]

        msg = compose_email_message(email_sender, email_receiver, data)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(email_sender, email_password)
            smtp.send_message(msg)
    except Exception as e:
        print("Error sending email: " + str(e))
