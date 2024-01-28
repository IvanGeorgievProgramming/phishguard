from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask

from app.config import Config
from app.utils.scheduler import remove_expired_routes

# Create the Flask app.
app = Flask(__name__)
# Load the config file.
app.config.from_object(Config)

# Create the temporary_routes dictionary.
temporary_routes = {}

# Create the scheduler.
scheduler = BackgroundScheduler()
scheduler.add_job(func=remove_expired_routes, args=[temporary_routes], trigger="interval", seconds=60)
scheduler.start()

# Import the routes.
from app.routes import routes
