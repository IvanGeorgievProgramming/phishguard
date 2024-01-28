from flask import render_template, request, url_for, redirect, abort
import json
import os
import time

from app import app, temporary_routes
from app.services.data_management.create_json_file import create_json_file
from app.services.data_management.insert_web_analysis_data import insert_web_analysis_data
from app.services.data_management.insert_phishing_features_data import insert_phishing_features_data
from app.services.data_management.insert_phishing_status_data import insert_phishing_status_data
from app.services.email_management.send_email import send_email
from app.utils.url_utils import generate_route_name

@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    """
    Summary: 
        The home route.

    Description: 
        If the request method is POST, get the website url and the analysis option from the form.\n
        Generate a route name for the website url.\n
        Create a json file for the route name.\n
        Insert the website analysis data into the json file.\n
        Insert the phishing features data into the json file.\n
        Insert the phishing status data into the json file.\n
        Add the route name, the website url and the file name to the temporary_routes dictionary.\n
        Redirect the user to the result route.\n
        If the request method is GET, render the home template.\n

    Arguments: 
        None: No arguments are required.

    Returns: 
        render_template: The home template.
        redirect: The result route.
    """
    if request.method == "POST":
        website_url = request.form.get("website_url")
        option = request.form.get("analysis_option", "2")
        print(website_url, option)
        
        encoded_route_name = generate_route_name(website_url)

        create_json_file(encoded_route_name)
        insert_web_analysis_data(encoded_route_name, website_url, option)
        insert_phishing_features_data(encoded_route_name)
        insert_phishing_status_data(encoded_route_name)

        temporary_routes[encoded_route_name] = {
            "url": website_url,
            "expiry": time.time() + 300,
            "file_name": encoded_route_name
        }

        return redirect(url_for("result", encoded_route_name=encoded_route_name))
    
    return render_template("home.html")

@app.route("/result/<path:encoded_route_name>", methods=["GET", "POST"])
def result(encoded_route_name):
    """
    Summary: 
        The result route.

    Description: 
        Get the route info from the temporary_routes dictionary.\n
        If the route info does not exist or the route has expired, abort the request.\n
        Get the data from the json file.\n
        If the request method is POST, get the user email from the form.\n
        If the user email exists, send the email to the user.\n
        Render the home template.\n
        If the request method is GET, render the result template.\n

    Arguments: 
        encoded_route_name (str): The encoded route name.

    Returns: 
        render_template: The home template.
        render_template: The result template.
        abort: The 404 error page.
    """
    route_info = temporary_routes.get(encoded_route_name)
    if not route_info or time.time() > route_info["expiry"]:
        abort(404)

    json_file_path = os.path.join("data", f"{encoded_route_name}.json")
    with open(json_file_path, "r") as file:
        data = json.load(file)

    if request.method == "POST":
        user_email = request.form.get("user_email")
        if user_email:
            try:
                send_email(user_email, data)
                return render_template("home.html", email=user_email)
            except Exception as e:
                return render_template("result.html", error=str(e))

    web_url = data["website_analysis"]["website_info"]["url"]
    web_title = data["website_analysis"]["website_info"]["title"]
    web_phishing_status = data["phishing_status"]

    return render_template("result.html", url=route_info["url"], data=data, web_url=web_url, web_title=web_title, web_phishing_status=web_phishing_status)
