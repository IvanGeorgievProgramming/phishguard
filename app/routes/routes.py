from flask import render_template, request, url_for, redirect, abort, flash, current_app
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

        temporary_routes_expiry_seconds = app.config["TEMPORARY_ROUTES_EXPIRY_SECONDS"]
        temporary_routes[encoded_route_name] = {
            "url": website_url,
            "expiry": time.time() + temporary_routes_expiry_seconds,
            "file_name": encoded_route_name
        }

        return redirect(url_for("result", encoded_route_name=encoded_route_name))
    
    return render_template("home.html")

@app.route("/result/<path:encoded_route_name>", methods=["GET", "POST"])
def result(encoded_route_name):
    route_info = temporary_routes.get(encoded_route_name)
    if not route_info or time.time() > route_info["expiry"]:
        http_status_not_found = current_app.config["HTTP_STATUS_NOT_FOUND"]
        abort(http_status_not_found)

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
    
    try:
        has_valid_email = app.config["HAS_VALID_EMAIL"]
    except Exception as e:
        has_valid_email = False

    try:
        if web_phishing_status is not None:
            if web_phishing_status == 0:
                title = "Legitimate Website"
            elif web_phishing_status == 1:
                title = "Phishing Website"
            else:
                title = "Result"
        else:
            title = "Result"
    except Exception as e:
        title = "Result"
        print(f"Error in result: {e}")


    if request.method == "POST":
        user_email = request.form.get("user_email")

        if not validate_and_check_email(user_email):
            render_template("result.html", title=title, url=route_info["url"], data=data, web_url=web_url, web_title=web_title, web_phishing_status=web_phishing_status, has_valid_email=has_valid_email)
        
        try:
            send_email(user_email, data)
            flash("Email sent successfully!", "success")
            return redirect(url_for("home"))
        except Exception as e:
            flash("Failed to send the email. Please try again later.", "error")
            render_template("result.html", title=title, url=route_info["url"], data=data, web_url=web_url, web_title=web_title, web_phishing_status=web_phishing_status, has_valid_email=has_valid_email)

    return render_template("result.html", title=title, url=route_info["url"], data=data, web_url=web_url, web_title=web_title, web_phishing_status=web_phishing_status, has_valid_email=has_valid_email)
