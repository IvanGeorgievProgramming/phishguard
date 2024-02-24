from app.utils.url_utils import is_relative_link, is_same_domain

def count_audio_links(soup, base_url):
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
