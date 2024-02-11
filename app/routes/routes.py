from flask import render_template, request, url_for, redirect, abort, flash
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
from app.utils.validate_and_check_email import validate_and_check_email
from app.utils.validate_and_check_website_url import validate_and_check_website_url

@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    """
    Summary: 
        The home route.

    Description: 
        If the request method is POST, get the website URL and analysis option from the form.\n
        If the website URL is not valid, render the home template.\n
        Generate a route name for the website URL.\n
        Create a json file for the website URL.\n
        Insert the website analysis data, phishing features data, and phishing status data into the database.\n
        Add the route info to the temporary_routes dictionary.\n
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
        
        if not validate_and_check_website_url(website_url):
            return render_template("home.html")
        
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
        If the route info does not exist or the route info has expired, abort with a 404 error.\n
        Load the website data from the json file.\n
        If the request method is POST, get the user email from the form.\n
        If the user email is not valid, render the result template.\n
        Send the email to the user.\n
        If the email is sent successfully, flash a success message and redirect the user to the home route.\n
        If the email is not sent successfully, flash an error message and render the result template.\n
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

    try:
        json_file_path = os.path.join("data", f"{encoded_route_name}.json")
        with open(json_file_path, "r") as file:
            data = json.load(file)

        web_url = data["website_analysis"]["website_info"]["url"]
        web_title = data["website_analysis"]["website_info"]["title"]
        web_phishing_status = data["phishing_status"]
    except Exception as e:
        flash("Failed to load the website data.", "error")
        return redirect(url_for("home"))

    if request.method == "POST":
        user_email = request.form.get("user_email")

        if not validate_and_check_email(user_email):
            render_template("result.html", url=route_info["url"], data=data, web_url=web_url, web_title=web_title, web_phishing_status=web_phishing_status)
        
        try:
            send_email(user_email, data)
            flash("Email sent successfully!", "success")
            return redirect(url_for("home"))
        except Exception as e:
            flash("Failed to send the email. Please try again later.", "error")
            render_template("result.html", url=route_info["url"], data=data, web_url=web_url, web_title=web_title, web_phishing_status=web_phishing_status)

    return render_template("result.html", url=route_info["url"], data=data, web_url=web_url, web_title=web_title, web_phishing_status=web_phishing_status)
