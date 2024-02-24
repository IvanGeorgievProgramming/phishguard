import json
import os

from app.services.phishing_detection.detect_phishing_features import detect_phishing_features

def insert_phishing_features_data(file_name):
    try:
        if not file_name.endswith(".json"):
            file_name += ".json"

        directory = "data"

        if not os.path.exists(directory):
            os.makedirs(directory)

        file_path = os.path.join(directory, file_name)

        with open(file_path, "r") as file:
            data = json.load(file)

        new_data = detect_phishing_features(data)

        with open(file_path, "w") as file:
            json.dump(new_data, file, indent=4)
    except Exception as e:
        print("Error inserting phishing features data: " + str(e))
