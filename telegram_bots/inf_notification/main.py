import telebot
import time
import requests
from bs4 import BeautifulSoup

def get_inf():
    response = requests.get('https://www.cbr.ru/currency_base/daily/')
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find_all('td', class_='')
    final_str = ''
    index1 = 5
    print(data)

    try:
        for i in range(len(data) // 5):
            final_str = final_str + f'{data[index1 - 2].text}: {data[index1 - 1].text}\n'
            index1 += 5

    except IndexError:
        pass

    return final_str

while True:
    if time.strftime('%M') == '11':
        response = requests.get('https://finance.rambler.ru/currencies/USD/')
        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.find('span', class_='_ZXx92_y CVUkSwiH')

        print('READDY')
        bot = telebot.TeleBot('TOKEN')
        bot.send_message(1392167370, get_inf())
        time.sleep(60)

