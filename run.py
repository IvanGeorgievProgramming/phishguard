from dotenv import load_dotenv

# Load the environment variables from the .env file.
load_dotenv()

# Import the app variable from the app package.
from app import app

# If the script is run directly from the command line, run the Flask app.
if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"], host=app.config["HOST"], port=app.config["PORT"])
