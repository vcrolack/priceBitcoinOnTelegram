from bs4 import BeautifulSoup
import requests
import schedule

def eth_scraping():

    url = requests.get('https://www.coingecko.com/es/monedas/ethereum')
    soup = BeautifulSoup(url.content, 'html.parser')
    result = soup.find('span', {'class': 'no-wrap'})
    format_result = result.text

    return format_result