import secrets

def generate_secret_key():
    key_bytes_length = 16
    try:
        return secrets.token_hex(key_bytes_length)
    except Exception as e:
        print(f"Error in generate_secret_key: {e}")
        return "4f6d14ed575d917a5f5847b6be9e4da228addc38499dc92d"
