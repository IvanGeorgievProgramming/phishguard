from dotenv import set_key

def validate_flask_keys(env_file_name, default_env_keys, env_keys):
    for key, default_value in default_env_keys.items():
        value_to_set = str(default_value) if isinstance(default_value, bool) else default_value
        
        if key in ["FLASK_DEBUG", "FLASK_HOST", "FLASK_PORT"]:
            if env_keys[key] != str(default_value):
                print(f"The following key is incorrect: {key}. Setting to default value: {default_value}")
                set_key(env_file_name, key, value_to_set)
            else:
                print(f"{key} is correct.")
