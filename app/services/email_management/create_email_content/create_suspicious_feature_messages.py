from flask import current_app

def create_suspicious_feature_messages(data):
    suspicious_status = current_app.config["SUSPICIOUS_STATUS"]
    
    try:
        suspicious_feature_messages = []

        all_suspicious_features_messages = {
            "ip_address_in_domain": "...",
            "long_url_length": "The URL is somewhat lengthy, which could be suspicious, though not definitively indicative of phishing.",
            "url_shortening_service": "...",
            "at_symbol_in_url": "...",
            "double_slash_redirect": "...",
            "prefix_suffix_in_domain": "...",
            "sub_domain_count": "The presence of multiple subdomains can be suspicious and merits caution, but it's not definitive proof of phishing.",
            "https_certificate_trust": "The absence of HTTPS or the presence of an untrusted certificate can be a suspicious sign, but it's not definitive evidence of phishing.",
            "domain_registration_length": "There are no creation or expiration dates available for the domain, which could be a suspicious sign.",
            "favicon_source_domain": "...",
            "non_standard_port_usage": "...",
            "https_token_in_domain": "...",
            "request_url_external_objects": "A significant number of external objects are hosted on other domains, which could be a suspicious sign.",
            "url_of_anchor_domain_match": "A considerable number of anchor elements are linking to different domains, which could be a suspicious sign.",
            "meta_script_link_tag_links": "A moderate percentage of links in <Script> and <Link> tags zre pointing to external resources, which could indicate suspicious activity.",
            "server_form_handler_integrity": "SFHs referring to a different domain than the webpage's can be suspicious, as legitimate sites rarely process information externally.",
            "abnormal_url_whois": "...",
            "website_redirection_count": "A website being redirected 2 to 3 times may raise suspicions, as it's uncommon but not definitive evidence of phishing.",
            "status_bar_customization_check": "...",
            "right_click_disable_feature": "...",
            "popup_window_information_request": "...",
            "iframe_redirection_usage": "...",
            "domain_age_check": "...",
            "dns_record_availability": "...",
            "statistical_reports_analysis": "..."
        }

        features_containing_suspicious_signs = [
            "long_url_length",
            "sub_domain_count",
            "https_certificate_trust",
            "domain_registration_length",
            "request_url_external_objects",
            "url_of_anchor_domain_match",
            "meta_script_link_tag_links",
            "server_form_handler_integrity",
            "website_redirection_count",
        ]

        features = data["phishing_features"]

        for feature in features:
            if features[feature] == suspicious_status:
                if feature in features_containing_suspicious_signs:
                    suspicious_feature_messages.append(all_suspicious_features_messages[feature])

        return suspicious_feature_messages
    except Exception as e:
        print("Error creating suspicious feature messages: " + str(e))
        return []
