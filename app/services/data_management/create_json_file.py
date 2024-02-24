import json
import os

def create_json_file(file_name):
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
                "ip_address_in_domain": 0.5,
                "long_url_length": 0.5,
                "url_shortening_service": 0.5,
                "at_symbol_in_url": 0.5,
                "double_slash_redirect": 0.5,
                "prefix_suffix_in_domain": 0.5,
                "sub_domain_count": 0.5,
                "https_certificate_trust": 0.5,
                "domain_registration_length": 0.5,
                "favicon_source_domain": 0.5,
                "non_standard_port_usage": 0.5,
                "https_token_in_domain": 0.5,
                "request_url_external_objects": 0.5,
                "url_of_anchor_domain_match": 0.5,
                "meta_script_link_tag_links": 0.5,
                "server_form_handler_integrity": 0.5,
                "abnormal_url_whois": 0.5,
                "website_redirection_count": 0.5,
                "status_bar_customization_check": 0.5,
                "right_click_disable_feature": 0.5,
                "popup_window_information_request": 0.5,
                "iframe_redirection_usage": 0.5,
                "domain_age_check": 0.5,
                "dns_record_availability": 0.5,
                "statistical_reports_analysis": 0.5
            },
            "phishing_status": 1
        }

        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print("Error creating JSON file: " + str(e))
