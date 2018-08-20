from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

# website for web scraping in python:
# https://realpython.com/python-web-scraping-practical-introduction/

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None

def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)


# Example of opening a saved html file
# from bs4 import BeautifulSoup
# raw_html = open('contrived.html').read()
# html = BeautifulSoup(raw_html, 'html.parser')

# to overcome scraping challenges (when no response after waiting a considerable amount of time
# response = requests.get(address, headers={
#     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0',
# })

result = simple_get('https://ca.global.nba.com/statistics/teamstats/?_ga=2.159429181.1031417642.1534789057-844316833.1527599393')

print(len(result))

