from app.utils.url_utils import is_relative_link, is_same_domain

def count_video_links(soup, base_url):
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
