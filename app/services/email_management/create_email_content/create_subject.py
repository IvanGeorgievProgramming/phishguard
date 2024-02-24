from datetime import datetime

def create_subject(data):
    try:
        url = data["website_analysis"]["website_info"]["url"]
        title = data["website_analysis"]["website_info"]["title"]
        analysis_date_time = datetime.now().strftime("%d.%m.%Y, %H:%M:%S")

        subject = f"PHISHGUARD Analysis Report for {url} ({title}) on {analysis_date_time}"

        return subject
    except Exception as e:
        print("Error creating subject: " + str(e))
        return "PHISHGUARD Analysis Report"
