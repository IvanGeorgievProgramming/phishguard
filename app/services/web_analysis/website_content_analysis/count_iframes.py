def count_iframes(soup):
    try:
        hidden_iframes_count = 0
        visible_iframes_count = 0

        iframe_tags = soup.find_all("iframe")
        for iframe_tag in iframe_tags:
            style = iframe_tag.get("style")
            if "display: none" in style or "visibility: hidden" in style:
                hidden_iframes_count += 1
            else:
                visible_iframes_count += 1

        return hidden_iframes_count, visible_iframes_count

    except Exception as e:
        print("Error counting iframes: " + str(e))
        return 0, 0
