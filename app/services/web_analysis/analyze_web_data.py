from bs4 import BeautifulSoup

from app.services.web_analysis.setup_driver import setup_driver
from app.services.web_analysis.extract_source_codes.extract_html.extract_html_source_codes import extract_html_source_codes
from app.services.web_analysis.extract_source_codes.extract_javascript.extract_javascript_source_codes import extract_javascript_source_codes
from app.services.web_analysis.website_info.find_favicon import find_favicon
from app.services.web_analysis.website_info.count_redirections import count_redirections
from app.services.web_analysis.website_content_analysis.count_img_links import count_img_links
from app.services.web_analysis.website_content_analysis.count_video_links import count_video_links
from app.services.web_analysis.website_content_analysis.count_audio_links import count_audio_links
from app.services.web_analysis.website_content_analysis.count_a_links import count_a_links
from app.services.web_analysis.website_content_analysis.count_script_links import count_script_links
from app.services.web_analysis.website_content_analysis.count_link_links import count_link_links
from app.services.web_analysis.website_content_analysis.count_form_links import count_form_links
from app.services.web_analysis.website_content_analysis.count_iframes import count_iframes
from app.services.web_analysis.website_security_analysis.set_is_status_bar_customized import set_is_status_bar_customized
from app.services.web_analysis.website_security_analysis.set_is_right_click_disabled import set_is_right_click_disabled
from app.services.web_analysis.website_security_analysis.set_is_popup_asking_personal_info import set_is_popup_asking_personal_info

def analyze_web_data(data, url, option):
    try:
        with setup_driver() as driver:
            driver.get(url)
            original_soup = BeautifulSoup(driver.page_source, "html.parser")

            # * Website Info

            title = driver.title
            favicon = find_favicon(original_soup)
            redirections_count = count_redirections(url)
            
            data["website_analysis"]["website_info"]["url"] = url
            data["website_analysis"]["website_info"]["title"] = title
            data["website_analysis"]["website_info"]["favicon"] = favicon
            data["website_analysis"]["website_info"]["redirections_count"] = redirections_count

            # * Website Content Analysis

            html_source_codes = extract_html_source_codes(url, option, driver)

            internal_img_links_count = 0
            external_img_links_count = 0
            relative_img_links_count = 0

            internal_video_links_count = 0
            external_video_links_count = 0
            relative_video_links_count = 0

            internal_audio_links_count = 0
            external_audio_links_count = 0
            relative_audio_links_count = 0

            internal_a_links_count = 0
            external_a_links_count = 0
            relative_a_links_count = 0

            internal_script_links_count = 0
            external_script_links_count = 0
            relative_script_links_count = 0

            internal_link_links_count = 0
            external_link_links_count = 0
            relative_link_links_count = 0

            blank_form_links_count = 0
            internal_form_links_count = 0
            external_form_links_count = 0
            relative_form_links_count = 0

            hidden_iframes_count = 0
            visible_iframes_count = 0

            for html_source_code in html_source_codes:
                soup = BeautifulSoup(html_source_code, "html.parser")
                
                img_counts = count_img_links(soup, url)
                internal_img_links_count += img_counts[0]
                external_img_links_count += img_counts[1]
                relative_img_links_count += img_counts[2]

                video_counts = count_video_links(soup, url)
                internal_video_links_count += video_counts[0]
                external_video_links_count += video_counts[1]
                relative_video_links_count += video_counts[2]

                audio_counts = count_audio_links(soup, url)
                internal_audio_links_count += audio_counts[0]
                external_audio_links_count += audio_counts[1]
                relative_audio_links_count += audio_counts[2]

                a_counts = count_a_links(soup, url)
                internal_a_links_count += a_counts[0]
                external_a_links_count += a_counts[1]
                relative_a_links_count += a_counts[2]

                script_counts = count_script_links(soup, url)
                internal_script_links_count += script_counts[0]
                external_script_links_count += script_counts[1]
                relative_script_links_count += script_counts[2]

                link_counts = count_link_links(soup, url)
                internal_link_links_count += link_counts[0]
                external_link_links_count += link_counts[1]
                relative_link_links_count += link_counts[2]

                form_counts = count_form_links(soup, url)
                blank_form_links_count += form_counts[0]
                internal_form_links_count += form_counts[1]
                external_form_links_count += form_counts[2]
                relative_form_links_count += form_counts[3]

                iframe_counts = count_iframes(soup)
                hidden_iframes_count += iframe_counts[0]
                visible_iframes_count += iframe_counts[1]
            
            data["website_analysis"]["website_content_analysis"]["img"]["internal_links_count"] = internal_img_links_count
            data["website_analysis"]["website_content_analysis"]["img"]["external_links_count"] = external_img_links_count
            data["website_analysis"]["website_content_analysis"]["img"]["relative_links_count"] = relative_img_links_count
            
            data["website_analysis"]["website_content_analysis"]["video"]["internal_links_count"] = internal_video_links_count
            data["website_analysis"]["website_content_analysis"]["video"]["external_links_count"] = external_video_links_count
            data["website_analysis"]["website_content_analysis"]["video"]["relative_links_count"] = relative_video_links_count

            data["website_analysis"]["website_content_analysis"]["audio"]["internal_links_count"] = internal_audio_links_count
            data["website_analysis"]["website_content_analysis"]["audio"]["external_links_count"] = external_audio_links_count
            data["website_analysis"]["website_content_analysis"]["audio"]["relative_links_count"] = relative_audio_links_count

            data["website_analysis"]["website_content_analysis"]["a"]["internal_links_count"] = internal_a_links_count
            data["website_analysis"]["website_content_analysis"]["a"]["external_links_count"] = external_a_links_count
            data["website_analysis"]["website_content_analysis"]["a"]["relative_links_count"] = relative_a_links_count

            data["website_analysis"]["website_content_analysis"]["script"]["internal_links_count"] = internal_script_links_count
            data["website_analysis"]["website_content_analysis"]["script"]["external_links_count"] = external_script_links_count
            data["website_analysis"]["website_content_analysis"]["script"]["relative_links_count"] = relative_script_links_count

            data["website_analysis"]["website_content_analysis"]["link"]["internal_links_count"] = internal_link_links_count
            data["website_analysis"]["website_content_analysis"]["link"]["external_links_count"] = external_link_links_count
            data["website_analysis"]["website_content_analysis"]["link"]["relative_links_count"] = relative_link_links_count

            data["website_analysis"]["website_content_analysis"]["form"]["blank_links_count"] = blank_form_links_count
            data["website_analysis"]["website_content_analysis"]["form"]["internal_links_count"] = internal_form_links_count
            data["website_analysis"]["website_content_analysis"]["form"]["external_links_count"] = external_form_links_count
            data["website_analysis"]["website_content_analysis"]["form"]["relative_links_count"] = relative_form_links_count

            data["website_analysis"]["website_content_analysis"]["iframe"]["hidden_count"] = hidden_iframes_count
            data["website_analysis"]["website_content_analysis"]["iframe"]["visible_count"] = visible_iframes_count

            # * Website Security Analysis

            javascript_source_codes = extract_javascript_source_codes(html_source_codes)

            data["website_analysis"]["website_security_analysis"]["is_status_bar_customized"] = set_is_status_bar_customized(javascript_source_codes)
            data["website_analysis"]["website_security_analysis"]["is_right_click_disabled"] = set_is_right_click_disabled(javascript_source_codes)
            data["website_analysis"]["website_security_analysis"]["is_popup_asking_personal_info"] = set_is_popup_asking_personal_info(javascript_source_codes)

            return data

    except Exception as e:
        print("Error analyzing website data: " + str(e))
        return None
