import os

def delete_json_file(file_name):
    try:
        if not file_name.endswith(".json"):
            file_name += ".json"

        directory = "data"

        file_path = os.path.join(directory, file_name)

        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            print(f"File not found: {file_path}")
    except Exception as e:
        print("Error deleting file: " + str(e))
