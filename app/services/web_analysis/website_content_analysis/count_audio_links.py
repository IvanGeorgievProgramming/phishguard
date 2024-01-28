from app.utils.url_utils import is_relative_link, is_same_domain

def count_audio_links(soup, base_url):
    """
    Summary: 
        Count all audio tag links in the soup object and return the count of internal, external and relative links.

    Description: 
        Create a set to store all processed audio tag links to avoid counting the same link multiple times.\n
        Create variables to store internal, external and relative audio tag links count.\n
        Find all audio tags in the soup object.\n
        For each audio tag, get the audio tag link.\n
        If the audio tag link is not in the processed audio tag links set, add it to the set.\n
        If the audio tag link is relative, increment relative audio tag links count.\n
        If the audio tag link is internal, increment internal audio tag links count.\n
        If the audio tag link is external, increment external audio tag links count.\n
        Return internal, external and relative audio tag links count.\n

    Arguments: 
        soup (BeautifulSoup): The soup object of the website content.
        base_url (str): The base url of the website.

    Returns: 
        internal_audio_links_count (int): The count of internal audio tag links.
        external_audio_links_count (int): The count of external audio tag links.
        relative_audio_links_count (int): The count of relative audio tag links.

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and 0, 0, 0 is returned.
    """
    try:
        processed_audio_links = set()
        internal_audio_links_count = 0
        external_audio_links_count = 0
        relative_audio_links_count = 0

        audio_tags = soup.find_all("audio", src=True)
        for audio_tag in audio_tags:
            audio_link = audio_tag["src"]
            if audio_link and audio_link not in processed_audio_links:
                processed_audio_links.add(audio_link)
                if is_relative_link(audio_link):
                    relative_audio_links_count += 1
                elif is_same_domain(audio_link, base_url):
                    internal_audio_links_count += 1
                else:
                    external_audio_links_count += 1

        return internal_audio_links_count, external_audio_links_count, relative_audio_links_count
        
    except Exception as e:
        print("Error counting audio tag links: " + str(e))
        return 0, 0, 0