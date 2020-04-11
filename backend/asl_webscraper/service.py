"""
* Project Name: ASL Dictionary
* File Name: service.py
* Programmer: Kai Prince
* Date: Fri, Apr 10, 2020
* Description: This file contains service functions for the Webscraper app.
"""

from requests import get, post
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

def search_handspeak(query):
    """ Consumes a search query, and produces a list of tuples. """
    pages = search_handspeak_for_page(query)

    results = []
    for page in pages:
        images = get_images_from_handspeak(page)
        results.append((page, images))

    return results


def get_images_from_handspeak(url):
    """ Consumes a URL, and produces a list of URLs. """
    image_links = get_images(url)

    filtered = filter_handspeak_images(image_links)
    return filtered


def filter_handspeak_images(image_links):
    """ Consumes a list of URLs, and produces a list of URLs. """

    BLACKLIST = [
        "https://www.handspeak.com/pix/hslogo2019.svg",
        "https://www.handspeak.com/write/asl/t/test.jpg",
    ]

    def not_in_blacklist(link):
        for item in BLACKLIST:
            if re.search(item, link):
                return False
        return True

    return list(filter(not_in_blacklist, image_links))


def search_handspeak_for_page(query):
    """ Consumes a search query, and produces a list of URLs. """

    url = "https://www.handspeak.com/word/search/app/app-dictionary.php"
    data = {"page": 1, "query": query}

    response = simple_post(url, data)
    html = BeautifulSoup(response, "html.parser")

    tags = html("a")

    links = set()
    for tag in tags:
        if tag["href"] == "#":
            continue

        link = "https://www.handspeak.com" + tag["href"]
        links.add(link)

    return links


def search_lifeprint(query):
    """ Consumes a search query, and produces a list of tuples. """
    pages = search_lifeprint_for_page(query)

    results = []
    for page in pages:
        images = get_images_from_lifeprint(page)
        results.append((page, images))

    return results


def search_lifeprint_for_images(query):
    """ Consumes a search query, and produces a list of URLs. """

    page_links = search_lifeprint_for_page(query)

    image_links = set()
    for page in page_links:
        links = get_images_from_lifeprint(page)
        image_links.update(links)

    return image_links


def get_index_url(query):
    base_wordlist_url = "https://www.lifeprint.com/asl101/index/{}.htm"

    first_letter = str.lower(query[0])

    url = base_wordlist_url.format(first_letter)

    return url


def search_lifeprint_for_page(query):
    """ Consumes a search query, and produces a List of URLs. """

    url = get_index_url(query)

    page = get_page(url)
    html = BeautifulSoup(page, "html.parser")

    tags = html.find_all("a", string=re.compile(query, re.IGNORECASE))

    links = set()
    for tag in tags:
        link = urljoin(url, tag["href"])
        links.add(link)

    return links


def get_images_from_lifeprint(url):
    """ Returns signing images from Lifeprint. """

    images = get_images(url)
    filtered = filter_lifeprint_images(images)

    return filtered


def filter_lifeprint_images(image_links):
    """ Consumes a list of URLs, and produces a list of URLs. """

    BLACKLIST = ["https://www.lifeprint.com/asl101/images-layout/"]

    def not_in_blacklist(link):
        for item in BLACKLIST:
            if re.search(item, link):
                return False
        return True

    return list(filter(not_in_blacklist, image_links))


def get_images(url):
    """ Returns full links to all images on a page. """

    page = get_page(url)
    html = BeautifulSoup(page, "html.parser")

    images = html.find_all("img")
    image_links = set()
    for image in images:
        link = urljoin(url, image["src"])
        image_links.add(link)

    return image_links


def get_page(url):
    """ Make a HTTP GET request to a given url, and return the response. """

    response = simple_get(url)

    return response


def simple_post(url, data):
    """
    Attempts to get the content at `url` by making an HTTP POST request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(post(url, data, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error("Error during requests to {0} : {1}".format(url, str(e)))
        return None


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
        log_error("Error during requests to {0} : {1}".format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers["Content-Type"].lower()
    return (
        resp.status_code == 200
        and content_type is not None
        and content_type.find("html") > -1
    )


def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)
