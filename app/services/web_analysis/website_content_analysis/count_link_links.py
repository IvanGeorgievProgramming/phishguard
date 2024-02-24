from app.utils.url_utils import is_relative_link, is_same_domain

def count_link_links(soup, base_url):
    try:
        processed_link_links = set()
        internal_link_links_count = 0
        external_link_links_count = 0
        relative_link_links_count = 0

        link_tags = soup.find_all("link", href=True)
        for link_tag in link_tags:
            link_link = link_tag["href"]
            if link_link and link_link not in processed_link_links:
                processed_link_links.add(link_link)
                if is_relative_link(link_link):
                    relative_link_links_count += 1
                elif is_same_domain(link_link, base_url):
                    internal_link_links_count += 1
                else:
                    external_link_links_count += 1

        return internal_link_links_count, external_link_links_count, relative_link_links_count
        
    except Exception as e:
        print("Error counting link tag links: " + str(e))
        return 0, 0, 0
