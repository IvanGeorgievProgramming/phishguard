from flask import flash
from email_validator import validate_email, EmailNotValidError

def validate_and_check_email(email):
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
