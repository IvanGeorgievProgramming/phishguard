from flask import current_app

def create_phishing_feature_messages(data):
    phishing_status = current_app.config["PHISHING_STATUS"]
    
    try:
        phishing_feature_messages = []
        all_phishing_feature_messages = {
            "ip_address_in_domain": "The website's URL contains an IP address, which is a common tactic used by phishers to obscure malicious domains.",
            "long_url_length": "The URL is longer than average, potentially hiding suspicious parts, a tactic often seen in phishing attempts.",
            "url_shortening_service": "The website uses a URL shortening service, which can be a method to conceal malicious links.",
            "at_symbol_in_url": "The presence of an '@' symbol in the URL can lead the browser to ignore everything preceding it, a trick used in phishing.",
            "double_slash_redirect": "The URL contains unexpected '//' characters, suggesting a redirection tactic often used in phishing.",
            "prefix_suffix_in_domain": "The domain name contains unusual prefixes or suffixes separated by dashes, a characteristic of phishing sites.",
            "sub_domain_count": "An excessive number of subdomains are used, a complexity often associated with phishing attempts.",
            "https_certificate_trust": "The absence of HTTPS and the presence of an untrusted certificate is a strong indicator of phishing.",
            "domain_registration_length": "The domain registration is set to expire within a year, which can be indicative of a phishing site.",
            "favicon_source_domain": "The favicon is loaded from an external domain, a tactic that could indicate a phishing attempt.",
            "non_standard_port_usage": "The website uses non-standard port numbers, which can be indicative of phishing or malicious activities.",
            "https_token_in_domain": "Including the 'HTTPS' token within the domain part is a deceptive tactic meant to mimic secure sites.",
            "request_url_external_objects": "A high percentage of external content comes from different domains, a common characteristic of phishing sites.",
            "url_of_anchor_domain_match": "The majority of anchor elements are linking to different domains, a tactic often used in phishing.",
            "meta_script_link_tag_links": "A high percentage of links in <Script> and <Link> tags lead to external domains, raising concerns of phishing.",
            "server_form_handler_integrity": "SFHs that are empty or direct to 'about:blank' are dubious, indicating potential phishing as they fail to specify an action for submitted information.",
            "abnormal_url_whois": "If the host name is not included in the URL, it suggests a lack of transparency common in phishing sites.",
            "website_redirection_count": "Websites with 4 or more redirects often indicate phishing attempts, aiming to confuse or mislead users.",
            "status_bar_customization_check": "Customizing the status bar with JavaScript, especially to show a fake URL on mouseover, is a deceptive practice used in phishing.",
            "right_click_disable_feature": "Preventing right-click functionality is a tactic used by phishers to obstruct users from inspecting the website's source code.",
            "popup_window_information_request": "Pop-up windows requesting personal information are often used by phishing sites to deceitfully collect user data.",
            "iframe_redirection_usage": "Iframes are commonly employed by phishers to stealthily redirect users, a tactic not typically seen on legitimate sites.",
            "domain_age_check": "A domain's age less than 6 months can be a red flag, as phishing sites frequently have a short lifespan.",
            "dns_record_availability": "Lack of a DNS record or unrecognized identity in WHOIS databases is a strong indicator of phishing.",
            "statistical_reports_analysis": "The website contains dangerous top-level domains, a common characteristic of phishing sites."
        }

        features = data["phishing_features"]

        for feature in features:
            if features[feature] == phishing_status:
                phishing_feature_messages.append(all_phishing_feature_messages[feature])

        return phishing_feature_messages
    except Exception as e:
        print("Error creating phishing feature messages: " + str(e))
        return []
