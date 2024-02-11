# 13
def evaluate_external_request_ratio(img_internal_links_count, img_external_links_count, img_relative_links_count, video_internal_links_count, video_external_links_count, video_relative_links_count, audio_internal_links_count, audio_external_links_count, audio_relative_links_count):
    """
    Summary: 
        Calculates the ratio of internal, external and relative links in the img, video and audio tags and returns a value based on the ratio.

    Description: 
        Calculates the total number of internal, external and relative links in the img, video and audio tags.\n
        If there are no external links, then the value returned is 0.\n
        A ratio is calculated based on the number of internal, external and relative links.\n
        If the ratio is less than 22%, then 0 is returned.\n
        If the ratio is between 22% and 61%, then 0.5 is returned.\n
        If the ratio is greater than 61%, then 1 is returned.\n

    Arguments: 
        img_internal_links_count (int): The number of internal links in all img tags.
        img_external_links_count (int): The number of external links in all img tags.
        img_relative_links_count (int): The number of relative links in all img tags.
        video_internal_links_count (int): The number of internal links in all video tags.
        video_external_links_count (int): The number of external links in all video tags.
        video_relative_links_count (int): The number of relative links in all video tags.
        audio_internal_links_count (int): The number of internal links in all audio tags.
        audio_external_links_count (int): The number of external links in all audio tags.
        audio_relative_links_count (int): The number of relative links in all audio tags.

    Returns: 
        (int): Either 0, 0.5 or 1

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and 0.5 is returned.
    """
    try:
        internal_links_count = img_internal_links_count + video_internal_links_count + audio_internal_links_count
        external_links_count = img_external_links_count + video_external_links_count + audio_external_links_count
        relative_links_count = img_relative_links_count + video_relative_links_count + audio_relative_links_count

        if external_links_count == 0:
            return 0
        
        ratio = (internal_links_count + relative_links_count) / external_links_count
        percentage = ratio * 100

        if percentage < 22.0:
            return 0
        elif percentage >= 22.0 and percentage < 61.0:
            return 0.5
        else:
            return 1
    except Exception as e:
        print(f"Error in evaluate_external_request_ratio: {e}")
        return 0.5
