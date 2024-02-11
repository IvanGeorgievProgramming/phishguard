def create_analysis_summary(data):
    """
    Summary: 
        Creates the analysis summary for the email content.

    Description:
        The phishing status is extracted from the data dictionary.\n
        The analysis summary is created based on the phishing status.\n
        If the phishing status is -1, the analysis summary indicates that the website is likely safe.\n
        If the phishing status is 1, the analysis summary indicates that the website may pose a potential phishing threat.\n
        The analysis summary is returned.\n

    Arguments:
        data (dict): The data dictionary containing the phishing status.

    Returns:
        analysis_summary (str): The analysis summary for the email content.

    Exceptions:
        In case of an exception during the execution of the function, an error message is printed to the console and an empty string is returned.
    """
    try:
        phishing_status = data["phishing_status"]
        analysis_summary = ""

        if phishing_status == 0:
            analysis_summary = "Our analysis indicates that this website is likely safe, with no immediate phishing threats detected. However, continue to browse with caution and stay vigilant."
        elif phishing_status == 1:
            analysis_summary = "Our analysis suggests that this website may pose a potential phishing threat. Please proceed with caution and consider the risks before sharing personal information."

        return analysis_summary
    except Exception as e:
        print("Error creating analysis summary: " + str(e))
        return ""
