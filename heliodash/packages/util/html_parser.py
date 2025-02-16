from urllib.error import HTTPError, URLError
from urllib.request import urlopen

from bs4 import BeautifulSoup


def get_bs(url):
    try:
        html = urlopen(url)
    except HTTPError:
        # print(e)
        return None
    except URLError:
        # print("The server could not be found!")
        return None
    else:
        bs = BeautifulSoup(html.read(), "html.parser")
        return bs
