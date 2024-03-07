from dotenv import load_dotenv

from env_assurance.ensure_environment_setup import ensure_environment_setup

ensure_environment_setup()
load_dotenv()

from app import app

if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"], host=app.config["HOST"], port=app.config["PORT"])
