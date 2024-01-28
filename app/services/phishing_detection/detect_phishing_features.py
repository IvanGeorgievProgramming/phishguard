from app.services.phishing_detection.phishing_features.check_ip_address_in_domain import check_ip_address_in_domain
from app.services.phishing_detection.phishing_features.evaluate_url_length import evaluate_url_length
from app.services.phishing_detection.phishing_features.assess_url_shortening_service import assess_url_shortening_service
from app.services.phishing_detection.phishing_features.inspect_at_symbol_in_url import inspect_at_symbol_in_url
from app.services.phishing_detection.phishing_features.verify_double_slash_position import verify_double_slash_position
from app.services.phishing_detection.phishing_features.analyze_dash_in_domain import analyze_dash_in_domain
from app.services.phishing_detection.phishing_features.count_subdomains_in_url import count_subdomains_in_url
from app.services.phishing_detection.phishing_features.validate_https_certification import validate_https_certification
from app.services.phishing_detection.phishing_features.check_domain_registration_duration import check_domain_registration_duration
from app.services.phishing_detection.phishing_features.evaluate_favicon_origin import evaluate_favicon_origin
from app.services.phishing_detection.phishing_features.assess_port_status import assess_port_status
from app.services.phishing_detection.phishing_features.inspect_https_token_in_domain import inspect_https_token_in_domain
from app.services.phishing_detection.phishing_features.evaluate_external_request_ratio import evaluate_external_request_ratio
from app.services.phishing_detection.phishing_features.assess_anchor_domain_similarity import assess_anchor_domain_similarity
from app.services.phishing_detection.phishing_features.check_tag_links_domain_congruence import check_tag_links_domain_congruence
from app.services.phishing_detection.phishing_features.validate_sfh_domain_relevance import validate_sfh_domain_relevance
from app.services.phishing_detection.phishing_features.verify_url_host_identity import verify_url_host_identity
from app.services.phishing_detection.phishing_features.count_website_redirections import count_website_redirections
from app.services.phishing_detection.phishing_features.check_status_bar_manipulation import check_status_bar_manipulation
from app.services.phishing_detection.phishing_features.detect_right_click_disablement import detect_right_click_disablement
from app.services.phishing_detection.phishing_features.evaluate_pop_up_content import evaluate_pop_up_content
from app.services.phishing_detection.phishing_features.inspect_iframe_usage import inspect_iframe_usage
from app.services.phishing_detection.phishing_features.assess_domain_age import assess_domain_age
from app.services.phishing_detection.phishing_features.check_dns_record_presence import check_dns_record_presence
from app.services.phishing_detection.phishing_features.analyze_statistical_report_ranking import analyze_statistical_report_ranking

def detect_phishing_features(data):
    """
    Summary: 
        Detects the phishing features of the website and adds them to the data dictionary.

    Description: 
        Extracts the required data from the data dictionary.\n
        Calls the functions to detect the phishing features.\n
        Adds the detected phishing features to the data dictionary.\n
        Returns the data dictionary.\n

    Arguments: 
        data (dict): The dictionary containing the data of the website.

    Returns: 
        data (dict): The dictionary containing the data of the website analysis with the phishing features.

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and None is returned.
    """
    try:
        url = data["website_analysis"]["website_info"]["url"]
        favicon = data["website_analysis"]["website_info"]["favicon"]
        redirections_count = data["website_analysis"]["website_info"]["redirections_count"]

        img_internal_links_count = data["website_analysis"]["website_content_analysis"]["img"]["internal_links_count"]
        img_external_links_count = data["website_analysis"]["website_content_analysis"]["img"]["external_links_count"]
        img_relative_links_count = data["website_analysis"]["website_content_analysis"]["img"]["relative_links_count"]

        video_internal_links_count = data["website_analysis"]["website_content_analysis"]["video"]["internal_links_count"]
        video_external_links_count = data["website_analysis"]["website_content_analysis"]["video"]["external_links_count"]
        video_relative_links_count = data["website_analysis"]["website_content_analysis"]["video"]["relative_links_count"]

        audio_internal_links_count = data["website_analysis"]["website_content_analysis"]["audio"]["internal_links_count"]
        audio_external_links_count = data["website_analysis"]["website_content_analysis"]["audio"]["external_links_count"]
        audio_relative_links_count = data["website_analysis"]["website_content_analysis"]["audio"]["relative_links_count"]

        a_internal_links_count = data["website_analysis"]["website_content_analysis"]["a"]["internal_links_count"]
        a_external_links_count = data["website_analysis"]["website_content_analysis"]["a"]["external_links_count"]
        a_relative_links_count = data["website_analysis"]["website_content_analysis"]["a"]["relative_links_count"]

        script_internal_links_count = data["website_analysis"]["website_content_analysis"]["script"]["internal_links_count"]
        script_external_links_count = data["website_analysis"]["website_content_analysis"]["script"]["external_links_count"]
        script_relative_links_count = data["website_analysis"]["website_content_analysis"]["script"]["relative_links_count"]

        link_internal_links_count = data["website_analysis"]["website_content_analysis"]["link"]["internal_links_count"]
        link_external_links_count = data["website_analysis"]["website_content_analysis"]["link"]["external_links_count"]
        link_relative_links_count = data["website_analysis"]["website_content_analysis"]["link"]["relative_links_count"]

        form_blank_links_count = data["website_analysis"]["website_content_analysis"]["form"]["blank_links_count"]
        form_external_links_count = data["website_analysis"]["website_content_analysis"]["form"]["external_links_count"]
        
        iframe_hidden_count = data["website_analysis"]["website_content_analysis"]["iframe"]["hidden_count"]
        iframe_visible_count = data["website_analysis"]["website_content_analysis"]["iframe"]["visible_count"]

        is_status_bar_customized = data["website_analysis"]["website_security_analysis"]["is_status_bar_customized"]
        is_right_click_disabled = data["website_analysis"]["website_security_analysis"]["is_right_click_disabled"]
        is_popup_asking_personal_info = data["website_analysis"]["website_security_analysis"]["is_popup_asking_personal_info"]

        ip_address_in_domain = check_ip_address_in_domain(url)
        data["phishing_features"]["ip_address_in_domain"] = ip_address_in_domain

        long_url_length = evaluate_url_length(url)
        data["phishing_features"]["long_url_length"] = long_url_length

        url_shortening_service = assess_url_shortening_service(url)
        data["phishing_features"]["url_shortening_service"] = url_shortening_service

        at_symbol_in_url = inspect_at_symbol_in_url(url)
        data["phishing_features"]["at_symbol_in_url"] = at_symbol_in_url

        double_slash_redirect = verify_double_slash_position(url)
        data["phishing_features"]["double_slash_redirect"] = double_slash_redirect

        prefix_suffix_in_domain = analyze_dash_in_domain(url)
        data["phishing_features"]["prefix_suffix_in_domain"] = prefix_suffix_in_domain

        sub_domain_count = count_subdomains_in_url(url)
        data["phishing_features"]["sub_domain_count"] = sub_domain_count

        https_certificate_trust = validate_https_certification(url)
        data["phishing_features"]["https_certificate_trust"] = https_certificate_trust

        domain_registration_length = check_domain_registration_duration(url)
        data["phishing_features"]["domain_registration_length"] = domain_registration_length

        favicon_source_domain = evaluate_favicon_origin(url, favicon)
        data["phishing_features"]["favicon_source_domain"] = favicon_source_domain

        non_standard_port_usage = assess_port_status(url)
        data["phishing_features"]["non_standard_port_usage"] = non_standard_port_usage

        https_token_in_domain = inspect_https_token_in_domain(url)
        data["phishing_features"]["https_token_in_domain"] = https_token_in_domain

        request_url_external_objects = evaluate_external_request_ratio(img_internal_links_count, img_external_links_count, img_relative_links_count, video_internal_links_count, video_external_links_count, video_relative_links_count, audio_internal_links_count, audio_external_links_count, audio_relative_links_count)
        data["phishing_features"]["request_url_external_objects"] = request_url_external_objects

        url_of_anchor_domain_match = assess_anchor_domain_similarity(a_internal_links_count, a_external_links_count, a_relative_links_count)
        data["phishing_features"]["url_of_anchor_domain_match"] = url_of_anchor_domain_match

        meta_script_link_tag_links = check_tag_links_domain_congruence(script_internal_links_count, script_external_links_count, script_relative_links_count, link_internal_links_count, link_external_links_count, link_relative_links_count)
        data["phishing_features"]["meta_script_link_tag_links"] = meta_script_link_tag_links

        server_form_handler_integrity = validate_sfh_domain_relevance(form_blank_links_count, form_external_links_count)
        data["phishing_features"]["server_form_handler_integrity"] = server_form_handler_integrity

        abnormal_url_whois = verify_url_host_identity(url)
        data["phishing_features"]["abnormal_url_whois"] = abnormal_url_whois

        website_redirection_count = count_website_redirections(redirections_count)
        data["phishing_features"]["website_redirection_count"] = website_redirection_count

        status_bar_customization_check = check_status_bar_manipulation(is_status_bar_customized)
        data["phishing_features"]["status_bar_customization_check"] = status_bar_customization_check

        right_click_disable_feature = detect_right_click_disablement(is_right_click_disabled)
        data["phishing_features"]["right_click_disable_feature"] = right_click_disable_feature

        popup_window_information_request = evaluate_pop_up_content(is_popup_asking_personal_info)
        data["phishing_features"]["popup_window_information_request"] = popup_window_information_request

        iframe_redirection_usage = inspect_iframe_usage(iframe_hidden_count, iframe_visible_count)
        data["phishing_features"]["iframe_redirection_usage"] = iframe_redirection_usage

        domain_age_check = assess_domain_age(url)
        data["phishing_features"]["domain_age_check"] = domain_age_check

        dns_record_availability = check_dns_record_presence(url)
        data["phishing_features"]["dns_record_availability"] = dns_record_availability

        statistical_reports_analysis = analyze_statistical_report_ranking(url)
        data["phishing_features"]["statistical_reports_analysis"] = statistical_reports_analysis

        return data
    
    except Exception as e:
        print(f"Error detecting phishing features: {e}")
        return None
