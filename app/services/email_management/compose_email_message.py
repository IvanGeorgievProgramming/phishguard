from email.message import EmailMessage

from app.services.email_management.create_email_content.create_subject import create_subject
from app.services.email_management.create_email_content.create_introduction import create_introduction
from app.services.email_management.create_email_content.create_analysis_summary import create_analysis_summary
from app.services.email_management.create_email_content.create_phishing_feature_messages import create_phishing_feature_messages
from app.services.email_management.create_email_content.create_suspicious_feature_messages import create_suspicious_feature_messages
from app.services.email_management.create_email_content.create_legitimate_feature_messages import create_legitimate_feature_messages

def compose_email_message(email_sender, email_receiver, data):
    """
    Summary: 
        Composes the email message.

    Description: 
        The message object is created.\n
        The subject, sender, and receiver are set.\n
        The introduction, analysis summary, and feature messages are created.\n
        The feature messages are joined together.\n
        The email content is created using the introduction, analysis summary, and feature messages.\n
        The email content is set.\n
        The message object is returned.\n

    Arguments: 
        email_sender (str): The email address of the sender.
        email_receiver (str): The email address of the receiver.
        data (dict): The data dictionary containing the analysis results.

    Returns: 
        msg (EmailMessage): The message object containing the email content.

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and None is returned.
    """
    try:
        msg = EmailMessage()
        msg["Subject"] = create_subject(data)
        msg["From"] = email_sender
        msg["To"] = email_receiver

        introduction = create_introduction(data)
        analysis_summary = create_analysis_summary(data)
        phishing_feature_messages = create_phishing_feature_messages(data)
        suspicious_feature_messages = create_suspicious_feature_messages(data)
        legitimate_feature_messages = create_legitimate_feature_messages(data)
        
        phishing_features = "\n - ".join(phishing_feature_messages)
        suspicious_features = "\n - ".join(suspicious_feature_messages)
        legitimate_features = "\n - ".join(legitimate_feature_messages)
        
        email_content = f"""Hello,\n\n{introduction}\n\nAnalysis Summary:\n - {analysis_summary}\n\nDetailed Analysis Findings:\nFeatures Indicating Potential Phishing:\n - {phishing_features}\n\nSuspicious Features:\n - {suspicious_features}\n\nFeatures Indicating Legitimacy:\n - {legitimate_features}\n\nDisclaimer:\nThis analysis is based on current algorithms and data, aiming to assess potential risks. It doesn’t guarantee absolute safety or risk. We encourage always practicing caution and online safety measures.\n\nThank you for trusting PHISHGUARD with your online safety concerns. Your vigilance is your first line of defense in maintaining online security.\n\nSincerely,\nThe Developer behind PHISHGUARD"""

        msg.set_content(email_content)

        return msg
    except Exception as e:
        print("Error composing email message: " + str(e))
        return None
