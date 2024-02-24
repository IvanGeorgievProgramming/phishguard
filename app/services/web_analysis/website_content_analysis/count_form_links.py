from app.utils.url_utils import is_relative_link, is_same_domain

def count_form_links(soup, base_url):
    try:
        processed_form_links = set()
        blank_form_links_count = 0
        internal_form_links_count = 0
        external_form_links_count = 0
        relative_form_links_count = 0

        form_tags = soup.find_all("form", action=True)
        for form_tag in form_tags:
            form_link = form_tag["action"]
            if form_link and form_link not in processed_form_links:
                processed_form_links.add(form_link)
                if is_relative_link(form_link):
                    if form_link == "":
                        blank_form_links_count += 1
                    else:
                        relative_form_links_count += 1
                elif is_same_domain(form_link, base_url):
                    internal_form_links_count += 1
                else:
                    external_form_links_count += 1

        return blank_form_links_count, internal_form_links_count, external_form_links_count, relative_form_links_count
        
    except Exception as e:
        print("Error counting form links: " + str(e))
        return 0, 0, 0, 0
