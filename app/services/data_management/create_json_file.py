import json
import os

def create_json_file(file_name):
    """
    Summary: 
        Creates a JSON file with the given file name.

    Description:
        If the file name does not end with ".json", then it is appended to the file name.\n
        If the "data" directory does not exist, then it is created.\n
        The file path is created by joining the "data" directory and the file name.\n
        The JSON file is created with a default structure.\n

    Arguments:
        file_name (str): The name of the JSON file to be created.

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

        data = {
            "website_analysis": {
                "website_info": {
                    "url": "",
                    "title": "",
                    "favicon": "",
                    "redirections_count": 0
                },
                "website_content_analysis": {
                    "img": {
                        "internal_links_count": 0,
                        "external_links_count": 0,
                        "relative_links_count": 0
                    },
                    "video": {
                        "internal_links_count": 0,
                        "external_links_count": 0,
                        "relative_links_count": 0
                    },
                    "audio": {
                        "internal_links_count": 0,
                        "external_links_count": 0,
                        "relative_links_count": 0
                    },
                    "a": {
                        "internal_links_count": 0,
                        "external_links_count": 0,
                        "relative_links_count": 0
                    },
                    "script": {
                        "internal_links_count": 0,
                        "external_links_count": 0,
                        "relative_links_count": 0
                    },
                    "link": {
                        "internal_links_count": 0,
                        "external_links_count": 0,
                        "relative_links_count": 0
                    },
                    "form": {
                        "blank_links_count": 0,
                        "internal_links_count": 0,
                        "external_links_count": 0,
                        "relative_links_count": 0
                    },
                    "iframe": {
                        "hidden_count": 0,
                        "visible_count": 0
                    }
                },
                "website_security_analysis": {
                    "is_status_bar_customized": None,
                    "is_right_click_disabled": None,
                    "is_popup_asking_personal_info": None
                }
            },
            "phishing_features": {
                "ip_address_in_domain": 0,
                "long_url_length": 0,
                "url_shortening_service": 0,
                "at_symbol_in_url": 0,
                "double_slash_redirect": 0,
                "prefix_suffix_in_domain": 0,
                "sub_domain_count": 0,
                "https_certificate_trust": 0,
                "domain_registration_length": 0,
                "favicon_source_domain": 0,
                "non_standard_port_usage": 0,
                "https_token_in_domain": 0,
                "request_url_external_objects": 0,
                "url_of_anchor_domain_match": 0,
                "meta_script_link_tag_links": 0,
                "server_form_handler_integrity": 0,
                "abnormal_url_whois": 0,
                "website_redirection_count": 0,
                "status_bar_customization_check": 0,
                "right_click_disable_feature": 0,
                "popup_window_information_request": 0,
                "iframe_redirection_usage": 0,
                "domain_age_check": 0,
                "dns_record_availability": 0,
                "statistical_reports_analysis": 0
            },
            "phishing_status": 0
        }

        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print("Error creating JSON file: " + str(e))
