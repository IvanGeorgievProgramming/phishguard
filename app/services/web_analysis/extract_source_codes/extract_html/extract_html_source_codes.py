from flask import current_app

from app.services.web_analysis.extract_source_codes.extract_html.extracting_methods.extract_html_complete_site_analysis import extract_html_complete_site_analysis
from app.services.web_analysis.extract_source_codes.extract_html.extracting_methods.extract_html_comprehensive_analysis import extract_html_comprehensive_analysis
from app.services.web_analysis.extract_source_codes.extract_html.extracting_methods.extract_html_focused_analysis import extract_html_focused_analysis
from app.services.web_analysis.extract_source_codes.extract_html.extracting_methods.extract_html_quick_analysis import extract_html_quick_analysis
from app.services.web_analysis.extract_source_codes.extract_html.extracting_methods.extract_html_default_analysis import extract_html_default_analysis

def extract_html_source_codes(url, option, driver):
    complete_site_analysis = current_app.config["COMPLETE_SITE_ANALYSIS"]
    comprehensive_analysis = current_app.config["COMPREHENSIVE_ANALYSIS"]
    focused_analysis = current_app.config["FOCUSED_ANALYSIS"]
    quick_analysis = current_app.config["QUICK_ANALYSIS"]

    try:
        html_source_codes = []

        if option == complete_site_analysis:
            html_source_codes = extract_html_complete_site_analysis(url, driver)

        elif option == comprehensive_analysis:
            html_source_codes = extract_html_comprehensive_analysis(url, driver)

        elif option == focused_analysis:
            html_source_codes = extract_html_focused_analysis(url, driver)

        elif option == quick_analysis:
            html_source_codes = extract_html_quick_analysis(url, driver)
        
        else:
            html_source_codes = extract_html_default_analysis(url, driver)

        return html_source_codes

    except Exception as e:
        print("Error extracting HTML source code: " + str(e))
        return None
