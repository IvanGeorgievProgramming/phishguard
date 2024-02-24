import json
import os

from app.services.ml_model.predict_phishing_status import predict_phishing_status

def insert_phishing_status_data(file_name):
    try:
        if not file_name.endswith(".json"):
            file_name += ".json"

        directory = "data"

        if not os.path.exists(directory):
            os.makedirs(directory)

        file_path = os.path.join(directory, file_name)

        with open(file_path, "r") as file:
            data = json.load(file)

        ip_address_in_domain = data["phishing_features"]["ip_address_in_domain"]
        long_url_length = data["phishing_features"]["long_url_length"]
        url_shortening_service = data["phishing_features"]["url_shortening_service"]
        at_symbol_in_url = data["phishing_features"]["at_symbol_in_url"]
        double_slash_redirect = data["phishing_features"]["double_slash_redirect"]
        prefix_suffix_in_domain = data["phishing_features"]["prefix_suffix_in_domain"]
        sub_domain_count = data["phishing_features"]["sub_domain_count"]
        https_certificate_trust = data["phishing_features"]["https_certificate_trust"]
        domain_registration_length = data["phishing_features"]["domain_registration_length"]
        favicon_source_domain = data["phishing_features"]["favicon_source_domain"]
        non_standard_port_usage = data["phishing_features"]["non_standard_port_usage"]
        https_token_in_domain = data["phishing_features"]["https_token_in_domain"]
        request_url_external_objects = data["phishing_features"]["request_url_external_objects"]
        url_of_anchor_domain_match = data["phishing_features"]["url_of_anchor_domain_match"]
        meta_script_link_tag_links = data["phishing_features"]["meta_script_link_tag_links"]
        server_form_handler_integrity = data["phishing_features"]["server_form_handler_integrity"]
        abnormal_url_whois = data["phishing_features"]["abnormal_url_whois"]
        website_redirection_count = data["phishing_features"]["website_redirection_count"]
        status_bar_customization_check = data["phishing_features"]["status_bar_customization_check"]
        right_click_disable_feature = data["phishing_features"]["right_click_disable_feature"]
        popup_window_information_request = data["phishing_features"]["popup_window_information_request"]
        iframe_redirection_usage = data["phishing_features"]["iframe_redirection_usage"]
        domain_age_check = data["phishing_features"]["domain_age_check"]
        dns_record_availability = data["phishing_features"]["dns_record_availability"]
        statistical_reports_analysis = data["phishing_features"]["statistical_reports_analysis"]

        phishing_features_array = [
            ip_address_in_domain,
            long_url_length,
            url_shortening_service,
            at_symbol_in_url,
            double_slash_redirect,
            prefix_suffix_in_domain,
            sub_domain_count,
            https_certificate_trust,
            domain_registration_length,
            favicon_source_domain,
            non_standard_port_usage,
            https_token_in_domain,
            request_url_external_objects,
            url_of_anchor_domain_match,
            meta_script_link_tag_links,
            server_form_handler_integrity,
            abnormal_url_whois,
            website_redirection_count,
            status_bar_customization_check,
            right_click_disable_feature,
            popup_window_information_request,
            iframe_redirection_usage,
            domain_age_check,
            dns_record_availability,
            statistical_reports_analysis
        ]

        data["phishing_status"] = predict_phishing_status(phishing_features_array)

        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print("Error inserting phishing status data: " + str(e))
