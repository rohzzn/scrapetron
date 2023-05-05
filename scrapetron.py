import requests
from bs4 import BeautifulSoup

def get_html(url, headers=None, cookies=None):
    """Send a GET request to the specified URL and return the response text."""
    response = requests.get(url, headers=headers, cookies=cookies)
    response.raise_for_status()  # raise an exception if the response is an error
    return response.text

def post_html(url, data=None, headers=None, cookies=None):
    """Send a POST request to the specified URL with the specified data and return the response text."""
    response = requests.post(url, data=data, headers=headers, cookies=cookies)
    response.raise_for_status()  # raise an exception if the response is an error
    return response.text

def get_soup(html, parser='html.parser'):
    """Parse the HTML text and return a BeautifulSoup object."""
    soup = BeautifulSoup(html, parser)
    return soup

def find_links(soup, attrs=None):
    """Find all links on the page that match the specified attributes and return them as a list."""
    if attrs:
        links = [link.get('href') for link in soup.find_all('a', attrs=attrs)]
    else:
        links = [link.get('href') for link in soup.find_all('a')]
    return links

def find_elements(soup, tag, attrs=None):
    """Find all elements on the page with the specified tag that match the specified attributes and return them as a list."""
    if attrs:
        elements = [element for element in soup.find_all(tag, attrs=attrs)]
    else:
        elements = [element for element in soup.find_all(tag)]
    return elements

def find_text(soup, tag, attrs=None):
    """Find the text content of all elements on the page with the specified tag that match the specified attributes and return them as a list."""
    elements = find_elements(soup, tag, attrs=attrs)
    text = [element.text for element in elements]
    return text

def find_title(soup):
    """Find the page title and return it as a string."""
    title = soup.find('title').text
    return title
