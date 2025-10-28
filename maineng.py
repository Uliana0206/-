import telebot
from telebot import types
import opred
import tok

bot = telebot.TeleBot(tok.token)

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, "Здравствуйте!")
    bot.send_message(message.chat.id, "Вы можете выбрать слово из списка или написать свое")
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Да', callback_data='yes'))
    markup.add(types.InlineKeyboardButton('Нет', callback_data='no'))
    bot.send_message(message.chat.id, 'Вам нужен список слов, которые я знаю?', reply_markup=markup)

    @bot.callback_query_handler(func=lambda callback: True)
    def callback(callback):
        if callback.data == "yes":
            bot.send_message(message.chat.id, "Список:Альтушка, Байтить, Вайб, Варик, Душнила, Жиза, Задрот, Запилить, Имба, Кринж, Криповый, Лейм, Мем, Мем, Пруфы, Чекать, Сас, Форсить, Фрик, Чиллить, Читер, ЧСВ, Шеймить, Шипперить")
            bot.send_message(message.chat.id, "Введите интересующее вас слово с заглавной буквы")
        else:
            bot.send_message(message.chat.id, "Введите интересующее вас слово с заглавной буквы")


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == "Вайб" or message.text == "Плюс вайб" or message.text == "Минус вайб":
            bot.send_message(message.chat.id, opred.vibe)
            bot.send_message(message.chat.id, "Так же слово Вайб используется в словосочитаниях ПЛЮС ВАЙБ и МИНУС ВАЙБ")
            bot.send_message(message.chat.id, "Минус вайб-ситуация огорчает,ухудшается общее эмоциональное состояние")
            bot.send_message(message.chat.id, "Плюс вайб-настроение поднимается,ситуация порадовала")
        elif message.text == "Имба":
            bot.send_message(message.chat.id, opred.imba)
        elif message.text == "Криповый":
            bot.send_message(message.chat.id, opred.krip)
        elif message.text == "Лейм":
            bot.send_message(message.chat.id, opred.lim)
        elif message.text == "Сас" or message.text == "Сасный":
            bot.send_message(message.chat.id, opred.sas)
        elif message.text == "Шеймить":
            bot.send_message(message.chat.id, opred.shim)
        elif message.text == "Шипперить" or message.text == "Шип" or message.text == "Шипирить" or message.text == "Шипп":
           bot.send_message(message.chat.id, opred.ship)
        elif message.text == "Чиллить" or message.text == "Чилить" or message.text == "Чилл" or message.text == "Чил":
            bot.send_message(message.chat.id, opred.chill)
        elif message.text == "Байтить":
            bot.send_message(message.chat.id, opred.bait)
        elif message.text == "Форсить":
            bot.send_message(message.chat.id, opred.fors)
        elif message.text == "Варик":
            bot.send_message(message.chat.id, opred.varic)
        elif message.text == "Душнила":
            bot.send_message(message.chat.id, opred.dush)
        elif message.text == "Жиза":
            bot.send_message(message.chat.id, opred.jiza)
        elif message.text == "Задрот":
            bot.send_message(message.chat.id, opred.zadrot)
        elif message.text == "Кринж":
            bot.send_message(message.chat.id, opred.kringe)
        elif message.text == "Запилить":
            bot.send_message(message.chat.id, opred.pil)
        elif message.text == "Пруфы":
            bot.send_message(message.chat.id, opred.pruf)
        elif message.text == "Чекать":
            bot.send_message(message.chat.id, opred.chec)
        elif message.text == "Читер":
            bot.send_message(message.chat.id, opred.chiter)
        elif message.text == "ЧСВ":
            bot.send_message(message.chat.id, opred.csv)
        elif message.text == "Мем":
            bot.send_message(message.chat.id, opred.mem)
        elif message.text == "Фрик":
            bot.send_message(message.chat.id, opred.frik)
        elif message.text == "Альтушка":
            bot.send_message(message.chat.id, opred.alit)
        elif message.text == "Муд":
            bot.send_message(message.chat.id, opred.mud)
        else:
            bot.send_message(message.chat.id, "К сожалению, я не знаю данного слова.")




bot.polling(none_stop=True)

