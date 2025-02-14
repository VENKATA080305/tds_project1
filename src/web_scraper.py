import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    """Scrape and extract text content from a webpage."""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.get_text()
