from dotenv import dotenv_values

def check_env_keys_existance(env_file_name, default_env_keys):
    loaded_env_keys = dotenv_values(env_file_name)

    for key, value in default_env_keys.items():
        if key not in loaded_env_keys:
            print(f"{key} not found. Adding to {env_file_name}.")
            with open(env_file_name, "a") as file:
                value_str = f"'{value}'" if isinstance(value, str) else f"'{str(value)}'"
                file.write(f"{key}={value_str}\n")
        else:
            print(f"{key} found.")
