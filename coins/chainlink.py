from bs4 import BeautifulSoup
import requests
import schedule

def link_scraping():
    url = requests.get('https://www.coingecko.com/es/monedas/chainlink')
    soup = BeautifulSoup(url.content, 'html.parser')
    result = soup.find('span', {'class': 'no-wrap'})
    format_result = result.text

    return format_result