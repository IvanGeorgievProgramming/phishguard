import requests

def count_redirections(url):
    try:
        response = requests.get(url)
        redirections_count = len(response.history)
        return redirections_count
    except Exception as e:
        print("Error counting redirections: " + str(e))
        return 0
