from datetime import datetime

def create_introduction(data):
    """
    Summary: 
        Creates the introduction for the email content.

    Description: 
        The URL and title of the website are extracted from the data dictionary.\n
        The current date and time are generated and formatted.\n
        The introduction uses the URL, title, and current date and time to create the introduction for the email content.\n
        The introduction is returned.\n

    Arguments: 
        data (dict): The data dictionary containing the website analysis results.

    Returns: 
        introduction (str): The introduction for the email content.

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and an empty string is returned.
    """
    try:
        url = data["website_analysis"]["website_info"]["url"]
        title = data["website_analysis"]["website_info"]["title"]
        analysis_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        introduction = f"Thank you for using PHISHGUARD to evaluate the safety of {url} ({title}).\nFollowing our analysis on {analysis_date_time}, here are our findings:"

        return introduction
    except Exception as e:
        print("Error creating introduction: " + str(e))
        return ""
