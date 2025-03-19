import telebot 
from telebot import types
bot = telebot.TeleBot('7284716165:AAEONRiBu80RvfZCTW37J-biXxe_WFdLrs4')
keyboard= types.ReplyKeyboardMarkup(resize_keyboard=True) # если несколько кнопок вы можете имспользовать row_width=2
button1 = types.KeyboardButton('Инфо о себе')   

keyboard.add(button1)


@bot.message_handler(commands=['start', 'hi'])
def start_message(message):
    message2 = bot.send_message(message.chat.id, 'Привет, напиши ифнормацию о себе, я сохраню это в файлах')
    bot.register_next_step_handler(message, save_info)

def save_info(message):
    try:
        with open('user_info.txt', 'a') as file:
            info = message.text
            file.write(info+'\n')
    except:
        bot.send_message(message.chat.id, 'Чтото пошло не так, попробуй заново!')
    else:
        bot.send_message(message.chat.id, 'Все успешно сохранилось!!!',reply_markup=keyboard)
    finally:
        print('ОК')

@bot.message_handler(content_types=['text'])
def send_info(message):
    if message.text.lower() == 'инфо о себе':
        with open('user_info.txt') as file:
            bot.send_document(message.chat.id, file)
    else:
        bot.send_message(message.chat.id, 'НАЖМИТЕ на кнопку!', reply_markup=keyboard)


bot.polling(non_stop=True, interval=0)