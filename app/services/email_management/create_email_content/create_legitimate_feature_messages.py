def create_legitimate_feature_messages(data):
    """
    Summary: 
        Creates the legitimate feature messages for the email content.

    Description: 
        A list of legitimate feature messages is created.\n
        A dictionary of all legitimate feature messages is created with the feature name as the key and the legitimate feature message as the value.\n
        The features dictionary is extracted from the data dictionary.\n
        For each feature in the features dictionary, if the feature value is -1, the corresponding message is added to the list of legitimate feature messages.\n
        The list of legitimate feature messages is returned.\n

    Arguments: 
        data (dict): The data dictionary containing the features.

    Returns: 
        legitimate_feature_messages (list): The list of legitimate feature messages.

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and an empty list is returned.
    """
    try:
        legitimate_feature_messages = []

        all_legitimate_features_messages = {
            "ip_address_in_domain": "The website's URL does not contain an IP address, which is typical for legitimate websites.",
            "long_url_length": "The URL length is within normal range, reducing suspicion of phishing attempts.",
            "url_shortening_service": "The website does not use URL shortening services, aligning with practices of legitimate sites.",
            "at_symbol_in_url": "The URL lacks an '@' symbol, avoiding common phishing tactics that exploit this character.",
            "double_slash_redirect": "The URL's use of '//' appears in the expected position, indicating normal behavior.",
            "prefix_suffix_in_domain": "The domain name does not use dashes in a suspicious manner, which is typical for legitimate domains.",
            "sub_domain_count": "The URL has a standard number of subdomains, suggesting a legitimate site.",
            "https_certificate_trust": "The site uses HTTPS with a trusted certificate issuer and an appropriate age, indicating a secure connection typical of legitimate websites.",
            "domain_registration_length": "The domain has a long-term registration, which is more common among trustworthy sites.",
            "favicon_source_domain": "The favicon is hosted on the same domain, consistent with legitimate website practices.",
            "non_standard_port_usage": "Standard port usage is observed, aligning with secure and legitimate website configurations.",
            "https_token_in_domain": "The website's domain does not misleadingly include 'HTTPS' in the domain part, avoiding confusion with secure protocols.",
            "request_url_external_objects": "A small percentage of external objects are loaded from different domains, indicating a legitimate website.",
            "url_of_anchor_domain_match": "Most anchor elements link to webpages within the same domain, suggesting a legitimate site.",
            "meta_script_link_tag_links": "A low percentage of links in <Meta>, <Script>, and <Link> tags are external, typical of legitimate websites.",
            "server_form_handler_integrity": "SFHs properly specify an action within the same domain, which is expected in legitimate websites.",
            "abnormal_url_whois": "The presence of the host name within the URL typically indicates a legitimate website, reflecting its identity clearly.",
            "website_redirection_count": "Websites redirected once or not at all are generally operating within the norms of legitimate online behavior.",
            "status_bar_customization_check": "Legitimate sites typically do not alter the status bar information, ensuring transparency and user trust.",
            "right_click_disable_feature": "Allowing right-click functionality is expected behavior, enabling users to interact fully with the website.",
            "popup_window_information_request": "Legitimate sites may use pop-up windows for announcements or warnings, without soliciting personal information through them.",
            "iframe_redirection_usage": "The use of iframes on legitimate sites is usually transparent, with visible borders and content relevant to the main site.",
            "domain_age_check": "Domains older than 6 months are often considered legitimate, as most phishing sites operate within shorter time frames.",
            "dns_record_availability": "A clear DNS record that matches the website's claimed identity supports its legitimacy.",
            "statistical_reports_analysis": "Sites not listed in statistical reports of phishing activity are more likely to be legitimate, assuming no other red flags are present."
        }

        features = data["phishing_features"]

        for feature in features:
            if features[feature] == -1:
                legitimate_feature_messages.append(all_legitimate_features_messages[feature])

        return legitimate_feature_messages
    except Exception as e:
        print("Error creating legitimate feature messages: " + str(e))
        return []