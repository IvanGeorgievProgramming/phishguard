# 13
from flask import current_app

def evaluate_external_request_ratio(img_internal_links_count, img_external_links_count, img_relative_links_count, video_internal_links_count, video_external_links_count, video_relative_links_count, audio_internal_links_count, audio_external_links_count, audio_relative_links_count):
    legitimate_status = current_app.config["LEGITIMATE_STATUS"]
    suspicious_status = current_app.config["SUSPICIOUS_STATUS"]
    phishing_status = current_app.config["PHISHING_STATUS"]
    suspicious_treshold_min = current_app.config["EXTERNAL_REQUEST_RATIO_SUSPICIOUS_THRESHOLD_MIN"]
    suspicious_treshold_max = current_app.config["EXTERNAL_REQUEST_RATIO_SUSPICIOUS_THRESHOLD_MAX"]
    
    try:
        internal_links_count = img_internal_links_count + video_internal_links_count + audio_internal_links_count
        external_links_count = img_external_links_count + video_external_links_count + audio_external_links_count
        relative_links_count = img_relative_links_count + video_relative_links_count + audio_relative_links_count

        if external_links_count == 0:
            return legitimate_status
        
        ratio = (internal_links_count + relative_links_count) / external_links_count
        percentage = ratio * 100

        if percentage < suspicious_treshold_min:
            return legitimate_status
        elif percentage >= suspicious_treshold_min and percentage < suspicious_treshold_max:
            return suspicious_status
        else:
            return phishing_status
    except Exception as e:
        print(f"Error in evaluate_external_request_ratio: {e}")
        return suspicious_status
