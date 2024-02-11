def create_suspicious_feature_messages(data):
    """
    Summary: 
        Creates the suspicious feature messages for the email content.

    Description: 
        A list of suspicious feature messages is created.\n
        A dictionary of all suspicious feature messages is created with the feature name as the key and the suspicious feature message as the value.\n
        The features dictionary is extracted from the data dictionary.\n
        For each feature in the features dictionary, if the feature's value is 0, the corresponding message is added to the list of suspicious feature messages.\n
        The list of suspicious feature messages is returned.\n

    Arguments: 
        data (dict): The data dictionary containing the features.

    Returns: 

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and an empty list is returned.
    """
    try:
        suspicious_feature_messages = []

        all_suspicious_features_messages = {
            "ip_address_in_domain": "The presence of an IP address in the URL could be a potential red flag, although it's not conclusive evidence of phishing.",
            "long_url_length": "The URL is somewhat lengthy, which could be suspicious, though not definitively indicative of phishing.",
            "url_shortening_service": "The use of a URL shortening service is not necessarily suspicious on its own, but it's a common practice in some phishing attempts.",
            "at_symbol_in_url": "The absence of an '@' symbol in the URL is generally expected and is not a cause for suspicion.",
            "double_slash_redirect": "The use of '//' characters in the URL seems normal and is not inherently suspicious.",
            "prefix_suffix_in_domain": "The absence of unusual prefixes or suffixes in the domain name is a good sign, but it doesn't rule out all potential phishing sites.",
            "sub_domain_count": "The presence of multiple subdomains can be suspicious and merits caution, but it's not definitive proof of phishing.",
            "https_certificate_trust": "The use of HTTPS is a positive sign, but if the certificate issuer is not well-known or the certificate is too new, it could raise some suspicion.",
            "domain_registration_length": "The domain's registration length is not suspicious on its own, but it's just one factor to consider when evaluating a website.",
            "favicon_source_domain": "The source of the favicon being hosted on an external domain is not typical for legitimate sites, which could raise suspicion.",
            "non_standard_port_usage": "The use of non-standard port numbers is not common among legitimate websites and may warrant caution.",
            "https_token_in_domain": "The inclusion of 'HTTPS' in the domain part can be a deceptive tactic, although it's not definitive evidence of phishing.",
            "request_url_external_objects": "A significant number of external objects hosted on other domains could be a suspicious sign and merits caution.",
            "url_of_anchor_domain_match": "A considerable number of anchor elements linking to external domains or not linking to any webpage could indicate suspicious activity.",
            "meta_script_link_tag_links": "A moderate percentage of links in <Script> and <Link> tags pointing to external resources may indicate cautious or suspicious design.",
            "server_form_handler_integrity": "SFHs referring to a different domain than the webpage's can be suspicious, as legitimate sites rarely process information externally.",
            "abnormal_url_whois": "The presence of the host name within the URL is generally expected for legitimate sites, reflecting their identity clearly.",
            "website_redirection_count": "A website being redirected 2 to 3 times may raise suspicions, as it's uncommon but not definitive evidence of phishing.",
            "status_bar_customization_check": "Customizing the status bar with JavaScript is an uncommon practice on legitimate sites and may be considered suspicious.",
            "right_click_disable_feature": "Disabling right-click functionality is not typical for legitimate sites and may raise some suspicion.",
            "popup_window_information_request": "Pop-up windows requesting personal information are highly suspicious and may indicate phishing attempts.",
            "iframe_redirection_usage": "The use of invisible iframes for redirection is not typically seen on legitimate sites and could raise suspicion.",
            "domain_age_check": "The age of the domain is not inherently suspicious, but phishing sites often have shorter lifespans.",
            "dns_record_availability": "The presence of a clear DNS record matching the website's claimed identity is a positive sign and reduces suspicion.",
            "statistical_reports_analysis": "Sites not listed in statistical reports of phishing activity are more likely to be legitimate, assuming no other red flags are present."
        }

        features = data["phishing_features"]

        for feature in features:
            if features[feature] == 0.5:
                suspicious_feature_messages.append(all_suspicious_features_messages[feature])

        return suspicious_feature_messages
    except Exception as e:
        print("Error creating suspicious feature messages: " + str(e))
        return []
