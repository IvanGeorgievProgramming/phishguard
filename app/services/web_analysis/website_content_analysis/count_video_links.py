from app.utils.url_utils import is_relative_link, is_same_domain

def count_video_links(soup, base_url):
    """
    Summary: 
        Count all video tag links in the soup object and return the count of internal, external and relative links.

    Description: 
        Create a set to store all processed video tag links to avoid counting the same link multiple times.\n
        Create variables to store internal, external and relative video tag links count.\n
        Find all video tags in the soup object.\n
        For each video tag, get the video tag link.\n
        If the video tag link is not in the processed video tag links set, add it to the set.\n
        If the video tag link is relative, increment relative video tag links count.\n
        If the video tag link is internal, increment internal video tag links count.\n
        If the video tag link is external, increment external video tag links count.\n
        Return internal, external and relative video tag links count.\n

    Arguments: 
        soup (BeautifulSoup): The soup object of the website content.
        base_url (str): The base url of the website.

    Returns: 
        internal_video_links_count (int): The count of internal video tag links.
        external_video_links_count (int): The count of external video tag links.
        relative_video_links_count (int): The count of relative video tag links.

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and 0, 0, 0 is returned.
    """
    try:
        processed_video_links = set()
        internal_video_links_count = 0
        external_video_links_count = 0
        relative_video_links_count = 0

        video_tags = soup.find_all("video", src=True)
        for video_tag in video_tags:
            video_link = video_tag["src"]
            if video_link and video_link not in processed_video_links:
                processed_video_links.add(video_link)
                if is_relative_link(video_link):
                    relative_video_links_count += 1
                elif is_same_domain(video_link, base_url):
                    internal_video_links_count += 1
                else:
                    external_video_links_count += 1

        return internal_video_links_count, external_video_links_count, relative_video_links_count
        
    except Exception as e:
        print("Error counting video links: " + str(e))
        return 0, 0, 0