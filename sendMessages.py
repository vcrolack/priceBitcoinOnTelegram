from bs4 import BeautifulSoup
import requests
import schedule
import coins.bitcoin as btc

def bot_send_text(bot_message):
    
    bot_token = '1720281467:AAFjixnqEFSiPHpboQjJ6J6oUHYYZ05SZ_Q'
    bot_chatID = '1331454134'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response

def report():
    btc_price = f'The price of Bitcoin today is {btc.btc_scraping()}'
    bot_send_text(btc_price)

if __name__ == '__main__':

    schedule.every().day.at("14:35").do(report)
    report()
    while True:
        schedule.run_pending()