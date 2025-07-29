import requests
from bs4 import BeautifulSoup

def scrape_example():
    url = 'https://example.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Modify based on actual content
    heading = soup.find('h1').text if soup.find('h1') else 'No heading found'
    return heading
