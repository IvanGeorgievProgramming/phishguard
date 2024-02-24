from dotenv import dotenv_values

from env_assurance.env_file_management.generate_secret_key.generate_secret_key import generate_secret_key
from env_assurance.env_file_management.env_file_existance.check_env_file_existance import check_env_file_existance
from env_assurance.env_file_management.env_keys_existance.check_env_keys_existance import check_env_keys_existance
from env_assurance.env_keys_management.flask_keys_validation.validate_flask_keys import validate_flask_keys
from env_assurance.env_keys_management.email_keys_validation.validate_email_keys import validate_email_keys

def ensure_environment_setup():
    env_file_name = ".env"
    default_env_keys = {
        "FLASK_DEBUG": False,
        "FLASK_HOST": "0.0.0.0",
        "FLASK_PORT": "5000",
        "SECRET_KEY": generate_secret_key(),
        "HAS_VALID_EMAIL": False,
        "EMAIL_SENDER": "",
        "EMAIL_PASSWORD": ""
    }

    print("Ensuring the .env file is set up correctly:\n")

    print(f"Checking {env_file_name}:")
    check_env_file_existance(env_file_name, default_env_keys)

    print("\nChecking the environment keys:")
    check_env_keys_existance(env_file_name, default_env_keys)

    env_keys = dotenv_values(env_file_name)

    print("\nValidating the flask keys:")
    validate_flask_keys(env_file_name, default_env_keys, env_keys)
    
    print("\nValidating the email keys:")
    validate_email_keys(env_file_name, env_keys)

    print("\nEnvironment setup complete.\n\n")
