import json
import os

from app.services.web_analysis.analyze_web_data import analyze_web_data

def insert_web_analysis_data(file_name, url, option):
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