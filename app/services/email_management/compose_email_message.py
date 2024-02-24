from email.message import EmailMessage
from flask import render_template
from datetime import datetime

from app.services.email_management.create_email_content.create_subject import create_subject
from app.services.email_management.create_email_content.create_phishing_feature_messages import create_phishing_feature_messages
from app.services.email_management.create_email_content.create_suspicious_feature_messages import create_suspicious_feature_messages
from app.services.email_management.create_email_content.create_legitimate_feature_messages import create_legitimate_feature_messages

def compose_email_message(email_sender, email_receiver, data):
    try:
        msg = EmailMessage()
        msg["Subject"] = create_subject(data)
        msg["From"] = email_sender
        msg["To"] = email_receiver

        url = data["website_analysis"]["website_info"]["url"]
        title = data["website_analysis"]["website_info"]["title"]
        date = datetime.now().strftime("%d.%m.%Y, %H:%M:%S")
        phishing_status = data["phishing_status"]

        phishing_feature_messages = create_phishing_feature_messages(data)
        suspicious_feature_messages = create_suspicious_feature_messages(data)
        legitimate_feature_messages = create_legitimate_feature_messages(data)

        html_content = render_template("email.html", url=url, title=title, date=date, phishing_status=phishing_status, phishing_feature_messages=phishing_feature_messages, suspicious_feature_messages=suspicious_feature_messages, legitimate_feature_messages=legitimate_feature_messages)
        msg.add_alternative(html_content, subtype="html")

        return msg
    except Exception as e:
        print("Error composing email message: " + str(e))
        return None
