from app.utils.url_utils import is_relative_link, is_same_domain

def count_script_links(soup, base_url):
    try:
        processed_script_links = set()
        internal_script_links_count = 0
        external_script_links_count = 0
        relative_script_links_count = 0

        script_tags = soup.find_all("script", src=True)
        for script_tag in script_tags:
            script_link = script_tag["src"]
            if script_link and script_link not in processed_script_links:
                processed_script_links.add(script_link)
                if is_relative_link(script_link):
                    relative_script_links_count += 1
                elif is_same_domain(script_link, base_url):
                    internal_script_links_count += 1
                else:
                    external_script_links_count += 1

        return internal_script_links_count, external_script_links_count, relative_script_links_count
        
    except Exception as e:
        print("Error counting script links: " + str(e))
        return 0, 0, 0
