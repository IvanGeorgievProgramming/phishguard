import os

# The Config class contains the configuration variables for the Flask app.
class Config:
    DEBUG = os.getenv("FLASK_DEBUG", "False") == "True"
    HOST = os.getenv("FLASK_HOST", "127.0.0.1")
    PORT = int(os.getenv("FLASK_PORT", "5000"))
    SECRET_KEY = os.getenv("SECRET_KEY")
    
    EMAIL_SENDER = os.getenv("EMAIL_SENDER")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
