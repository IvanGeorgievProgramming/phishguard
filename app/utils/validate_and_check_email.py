from flask import flash
from email_validator import validate_email, EmailNotValidError

def validate_and_check_email(email):
    """
    Summary: 
        Validate and check the email.

    Description: 
        If the email is empty, flash an error message and return False.\n
        If the email is not valid, flash an error message and return False.\n
        If the email is valid, return True.\n

    Arguments: 
        email (str): The email.

    Returns: 
        (bool): Either True or False.
    """
    if not email:
        flash("Email is required.", "error")
        return False
    
    try:
        valid = validate_email(email)
        normalized_email = valid.email
    except EmailNotValidError as e:
        flash(str(e), "error")
        return False

    return True
