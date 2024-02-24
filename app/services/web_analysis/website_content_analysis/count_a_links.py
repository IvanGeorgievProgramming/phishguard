from app.utils.url_utils import is_relative_link, is_same_domain

def count_a_links(soup, base_url):
    try:
        processed_a_links = set()
        internal_a_links_count = 0
        external_a_links_count = 0
        relative_a_links_count = 0

        a_tags = soup.find_all("a", href=True)
        for a_tag in a_tags:
            a_link = a_tag["href"]
            if a_link and a_link not in processed_a_links:
                processed_a_links.add(a_link)
                if is_relative_link(a_link):
                    relative_a_links_count += 1
                elif is_same_domain(a_link, base_url):
                    internal_a_links_count += 1
                else:
                    external_a_links_count += 1

        return internal_a_links_count, external_a_links_count, relative_a_links_count
        
    except Exception as e:
        print("Error counting a tag links: " + str(e))
        return 0, 0, 0
