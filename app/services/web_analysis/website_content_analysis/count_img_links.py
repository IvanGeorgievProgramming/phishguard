from app.utils.url_utils import is_relative_link, is_same_domain

def count_img_links(soup, base_url):
    try:
        processed_img_links = set()
        internal_img_links_count = 0
        external_img_links_count = 0
        relative_img_links_count = 0

        img_tags = soup.find_all("img", src=True)
        for img_tag in img_tags:
            img_link = img_tag["src"]
            if img_link and img_link not in processed_img_links:
                processed_img_links.add(img_link)
                if is_relative_link(img_link):
                    relative_img_links_count += 1
                elif is_same_domain(img_link, base_url):
                    internal_img_links_count += 1
                else:
                    external_img_links_count += 1

        return internal_img_links_count, external_img_links_count, relative_img_links_count
        
    except Exception as e:
        print("Error counting img tag links: " + str(e))
        return 0, 0, 0
