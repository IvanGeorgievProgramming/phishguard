from datetime import datetime

def create_subject(data):
    """
    Summary: 
        Creates the subject for the email.

    Description: 
        The URL and title of the website are extracted from the data dictionary.\n
        The current date and time are generated and formatted.\n
        The subject uses the URL, title, and current date and time to create the subject for the email.\n
        The subject is returned.\n

    Arguments: 
        data (dict): The data dictionary containing the website analysis results.

    Returns: 
        subject (str): The subject for the email.

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and a default subject is returned.
    """
    try:
        url = data["website_analysis"]["website_info"]["url"]
        title = data["website_analysis"]["website_info"]["title"]
        analysis_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        subject = f"PHISHGUARD Analysis Report for {url} ({title}) on {analysis_date_time}"

        return subject
    except Exception as e:
        print("Error creating subject: " + str(e))
        return "PHISHGUARD Analysis Report"
