import os

def delete_json_file(file_name):
    """
    Summary: 
        Deletes a JSON file with the given file name.

    Description: 
        If the file name does not end with ".json", then it is appended to the file name.\n
        If the "data" directory does not exist, then it is created.\n
        The file path is created by joining the "data" directory and the file name.\n
        If the file exists, then it is deleted.\n

    Arguments: 
        file_name (str): The name of the JSON file to be deleted.

    Returns: 
        None: This function does not return anything.

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console.
    """
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