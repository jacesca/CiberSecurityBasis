"""
Check the secure of a website based on:
- Website web protocol
"""
import requests


def check_web_site(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            if response.url.startswith('https'):
                return f"The website {url} uses HTTPS. It is secure."
            else:
                return f"The website {url} does not use HTTPS. It is not secure."  # noqa
        else:
            return f"Error: Unable to connect to {url}."
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"


if __name__ == '__main__':
    url_to_check = 'http://gmail.com'
    result = check_web_site(url_to_check)
    print(result)
