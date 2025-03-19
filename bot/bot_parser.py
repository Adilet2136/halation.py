
import telebot
from bs4 import BeautifulSoup as bs
import requests


bot = telebot.TeleBot('7284716165:AAEONRiBu80RvfZCTW37J-biXxe_WFdLrs4')
keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
button1 = telebot.types.KeyboardButton('НОУтбки')
button2 = telebot.types.KeyboardButton('телефоны')
keyboard.add(button1, button2)

@bot.message_handler(commands=['start'])
def start_message(message):
    message2= bot.send_message(message.chat.id , 'привет могу спарсить страницу Kivano.kg',reply_markup=keyboard)
    reply_markup=keyboard
    bot.register_next_step_handler(message2, handler)

def handler(message):
    if message.text.lower() == 'телефоны':
        parsing_telephone('https://www.kivano.kg/mobilnye-telefony', message)
    elif message.text.lower() == 'ноутбоки':
        parsing_laptop('https://www.kivano.kg/noutbuki-i-kompyutery')
    else:
        bot.send_message(message.chat.id, 'Haжми на кнопу', reply_markup=keyboard)

def parsing_telephone(url, message):
    html = requests.get(url).text
    soup = bs(html, 'lxml')
    telephones = soup.find_all('div', class_='item product_listbox oh')
    for telefon in telephones:
        link = telefon.find('a').get('href')
        title = telefon.find('img').get('alt')
        bot.send_message(message.chat.id, f'Телефон - {title}\nСсылка - https://www.kivano.kg{link}')



def parsing_laptop(url):
    html = requests.get(url).text
    soup = bs(html, 'lxml')

bot.polling(non_stop=True,interval=0)
