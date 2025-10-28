import telebot
from telebot import types
import opred
import tok
import fich

bot = telebot.TeleBot(tok.token)

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, "Здравствуйте! Я - СленГид, чат-бот, созданый для того, чтобы помочь вам понимать сленг!")
    bot.send_message(message.chat.id, 'Я не только расскажу вам, что значит данное слово, но и преведу пример предложения с этим словом')
    bot.send_message(message.chat.id, "Вы можете выбрать слово из списка или написать свое")
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Да', callback_data='yes'))
    markup.add(types.InlineKeyboardButton('Нет', callback_data='no'))
    bot.send_message(message.chat.id, 'Вам нужен список слов, которые я знаю?', reply_markup=markup)

    @bot.callback_query_handler(func=lambda callback: True)
    def callback(callback):
        if callback.data == "yes":
            bot.send_message(message.chat.id,
                             "Список:Альтушка, Баг, Байтить, Вайб, Варик, Донатить, Душнила, Жиза, Задрот, Запилить, Зашквар, Зумер, Ивейтить, Имба, Кринж, Криповый, Лейм, ЛС, Мем, Мерч, Муд, Мьют, Пруфы, Пушка, Рак, Рандом, Рофл, Сас, Сигма, Стэнить, Тейк, Топ, Треш, Ту мач, Фича, Форсить, Фрик, Хейтер, Чекать, Чиллить, Читер, ЧСВ, Шарить, Шеймить, Шипперить")
            bot.send_message(message.chat.id, "Введите интересующее вас слово с заглавной буквы")
        else:
            bot.send_message(message.chat.id, "Введите интересующее вас слово с заглавной буквы")


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == "Вайб" or message.text == "Плюс вайб" or message.text == "Минус вайб" or message.text == "Вайбовый":
            fich.vibe(message)
        elif message.text == "Имба" or message.text == "Имбовый" or message.text == "Имбища":
            fich.imba(message)
        elif message.text == "Криповый":
            fich.krip(message)
        elif message.text == "Лейм":
            fich.lim(message)
        elif message.text == "Сас" or message.text == "Сасный":
            fich.sas(message)
        elif message.text == "Шеймить":
            fich.shim(message)
        elif message.text == "Шипперить" or message.text == "Шип" or message.text == "Шипирить" or message.text == "Шипп":
           fich.ship(message)
        elif message.text == "Чиллить" or message.text == "Чилить" or message.text == "Чилл" or message.text == "Чил":
            fich.chill(message)
        elif message.text == "Байтить":
            fich.bait(message)
        elif message.text == "Форсить":
            fich.fors(message)
        elif message.text == "Варик":
            fich.varic(message)
        elif message.text == "Душнила" or message.text == "Душный":
            fich.dush(message)
        elif message.text == "Жиза":
            bot.send_message(message.chat.id, opred.jiza)
        elif message.text == "Задрот":
            fich.zadrot(message)
        elif message.text == "Кринж" or message.text == "Кринжовый" or message.text == "Кринжевать" :
            fich.kringe(message)
        elif message.text == "Запилить":
            fich.pil(message)
        elif message.text == "Пруфы":
            fich.pruf(message)
        elif message.text == "Чекать":
            fich.check(message)
        elif message.text == "Читер":
            fich.chiter(message)
        elif message.text == "ЧСВ":
            fich.csv(message)
        elif message.text == "Мем":
            fich.mem(message)
        elif message.text == "Фрик":
            fich.fric(message)
        elif message.text == "Альтушка":
            fich.alit(message)
        elif message.text == "Муд":
            bot.send_message(message.chat.id, opred.mud)
        elif message.text == "Донатить" or message.text == "Донат":
            fich.don(message)
        elif message.text == "Зашквар" or message.text == "Зашкварный":
            fich.zashkvar(message)
        elif message.text == "Зумер":
            bot.send_message(message.chat.id, opred.zum)
        elif message.text == "Пушка":
            bot.send_message(message.chat.id, opred.push)
        elif message.text == "Рак":
            bot.send_message(message.chat.id, opred.rak)
        elif message.text == "Рандом" or message.text == "Рандомный":
            fich.rand(message)
        elif message.text == "Хейтер" or message.text == "Хейтерить":
            fich.hait(message)
        elif message.text == "Ивейтить":
            bot.send_message(message.chat.id, opred.invate)
        elif message.text == "ЛС":
            fich.ls(message)
        elif message.text == "Мерч" or message.text == "Мерчовка":
            fich.merch(message)
        elif message.text == "Мьют":
            fich.mut(message)
        elif message.text == "Рофл" or message.text == "Рофлить" or message.text == "Рофельный":
            fich.rofl(message)
        elif message.text == "Сигма":
            fich.sigma(message)
        elif message.text == "Стэнить":
            fich.stem(message)
        elif message.text == "Тейк":
            fich.tik(message)
        elif message.text == "Топ" or message.text == "Топовый":
            fich.top(message)
        elif message.text == "Треш" or message.text == "Трешовый":
            fich.tresh(message)
        elif message.text == "Ту мач":
            fich.tu(message)
        elif message.text == "Фича":
            fich.ficha(message)
        elif message.text == "Шарить":
            fich.sharit(message)
        elif message.text == "Баг":
            fich.bag(message)
        elif message.text == "Буллинг" or message.text == "Буллить" or message.text == "Булинг" or message.text == "Булить":
            fich.bull(message)
        elif message.text == "Краш" or message.text == "Крашиха":
            fich.krash(message)
        elif message.text == "Ливнуть":
            fich.liv(message)
        else:
            bot.send_message(message.chat.id, "К сожалению, я не знаю данного слова.")

bot.polling(none_stop=True)


