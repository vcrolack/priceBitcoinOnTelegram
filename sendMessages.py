from bs4 import BeautifulSoup
import requests
import schedule
import coins.bitcoin as btc
import coins.polkadot as dot
import coins.ethereum as eth
import coins.chainlink as link
import coins.doge_coin as doge

def bot_send_text(bot_message):
    
    bot_token = '1720281467:AAFjixnqEFSiPHpboQjJ6J6oUHYYZ05SZ_Q'
    bot_chatID = '1331454134'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response

def report():
    btc_price = f'The price of Bitcoin today is {btc.btc_scraping()}'
    dot_price = f'The price of Polkadot today is {dot.dot_scraping()}'
    eth_price = f'The price of Ethereum today is {eth.eth_scraping()}'
    link_price = f'The price of Chainlink today is {link.link_scraping()}'
    doge_price = f'The price of Doge Coin today is {doge.doge_scraping()}'
    bot_send_text(btc_price)
    bot_send_text(dot_price)
    bot_send_text(eth_price)
    bot_send_text(link_price)
    bot_send_text(doge_price)


if __name__ == '__main__':

    schedule.every().day.at("14:35").do(report)
    report()
    while True:
        schedule.run_pending()