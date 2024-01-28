import json
import os

from app.services.web_analysis.analyze_web_data import analyze_web_data

def insert_web_analysis_data(file_name, url, option):
    """
    Summary: 
        Inserts web analysis data into a JSON file with the given file name.

    Description:
        If the file name does not end with ".json", then it is appended to the file name.\n
        If the "data" directory does not exist, then it is created.\n
        The file path is created by joining the "data" directory and the file name.\n
        The JSON file is opened and its data is loaded.\n
        The web analysis data is analyzed and inserted into the JSON file.\n
        The JSON file is opened and its data is dumped.\n

    Arguments:
        file_name (str): The name of the JSON file to insert web analysis data into.
        url (str): The URL of the website to be analyzed.
        option (int): The option of the web analysis.

    Returns:
        None: This function does not return anything.

    Exceptions:
        In case of an exception during the execution of the function, an error message is printed to the console.
    """
    try:
        if not file_name.endswith(".json"):
            file_name += ".json"

        directory = "data"

        if not os.path.exists(directory):
            os.makedirs(directory)

        file_path = os.path.join(directory, file_name)

        with open(file_path, "r") as file:
            data = json.load(file)

        new_data = analyze_web_data(data, url, option)

        with open(file_path, "w") as file:
            json.dump(new_data, file, indent=4)
    except Exception as e:
        print("Error inserting web analysis data: " + str(e))