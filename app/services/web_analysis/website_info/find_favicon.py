def find_favicon(soup):
    try:
        link_tags = soup.find_all("link")
        for link_tag in link_tags:
            if link_tag.get("rel") and "icon" in link_tag["rel"]:
                return link_tag.get("href")
        return ""
    except Exception as e:
        print("Error finding favicon: " + str(e))
        return ""
