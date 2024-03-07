from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask

from app.config import Config
from app.utils.remove_expired_routes import remove_expired_routes

app = Flask(__name__)
app.config.from_object(Config)

temporary_routes = {}

scheduler = BackgroundScheduler()
scheduler.add_job(func=remove_expired_routes, args=[temporary_routes], trigger="interval", seconds=app.config["SCHEDULER_INTERVAL_SECONDS"])
scheduler.start()

from app.routes import routes
