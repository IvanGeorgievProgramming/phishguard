import os

def check_env_file_existance(env_file_name, default_env_keys):
    if not os.path.exists(env_file_name):
        print(f"{env_file_name} not found. Creating with default values.")
        with open(env_file_name, "w") as file:
            for key, value in default_env_keys.items():
                value_str = f"'{value}'" if isinstance(value, str) else f"'{str(value)}'"
                file.write(f"{key}={value_str}\n")
    else:
        print(f"{env_file_name} found.")
