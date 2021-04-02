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
    btc_price = f'{btc.btc_scraping()}'
    dot_price = f'{dot.dot_scraping()}'
    eth_price = f'{eth.eth_scraping()}'
    link_price = f'{link.link_scraping()}'
    doge_price = f'{doge.doge_scraping()}'
    report_done = f'Greetings, user!\nThe price of the following cryptocurrencies are:BTC: {btc_price}\nDOT: {dot_price}\nETH: {eth_price}\nLINK: {link_price}\nDOGE: {doge_price}'
    bot_send_text(report_done)


if __name__ == '__main__':

    schedule.every().day.at("14:35").do(report)
    report()
    while True:
        schedule.run_pending()