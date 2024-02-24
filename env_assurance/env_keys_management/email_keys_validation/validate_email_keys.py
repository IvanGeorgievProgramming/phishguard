from dotenv import set_key

from env_assurance.env_keys_management.email_keys_validation.verify_email_credentials import verify_email_credentials

def validate_email_keys(env_file_name, env_keys):
    email_verified = False
    email_sender = env_keys["EMAIL_SENDER"]
    email_password = env_keys["EMAIL_PASSWORD"]

    if verify_email_credentials(email_sender, email_password):
        print("Email verified successfully.")
        email_verified = True
        set_key(env_file_name, "HAS_VALID_EMAIL", "True")
    else:
        response = input("Email verification failed. Would you like to type your email credentials manually? (y/n): ")
        if response.lower() != 'y':
            print("Email verification failed. Email functionality will be disabled.")
            set_key(env_file_name, "HAS_VALID_EMAIL", "False")
        else:
            while not email_verified:
                email_sender = input("Please enter your email sender: ")
                email_password = input("Please enter your email password: ")
                
                if verify_email_credentials(email_sender, email_password):
                    print("Email verified successfully.")
                    set_key(env_file_name, "HAS_VALID_EMAIL", "True")
                    set_key(env_file_name, "EMAIL_SENDER", email_sender)
                    set_key(env_file_name, "EMAIL_PASSWORD", email_password)
                    email_verified = True
                else:
                    response = input("Email verification failed. Would you like to try again? (y/n): ")
                    if response.lower() != 'y':
                        print("Email verification failed. Email functionality will be disabled.")
                        set_key(env_file_name, "HAS_VALID_EMAIL", "False")
                        break
