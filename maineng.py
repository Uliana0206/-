import telebot
from telebot import types
import opred
import tok
import primer

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
        if message.text == "Вайб" or message.text == "Плюс вайб" or message.text == "Минус вайб" or message.text == "Вайбовый":
            bot.send_message(message.chat.id, opred.vibe)
            bot.send_message(message.chat.id, primer.vibepr)
            bot.send_message(message.chat.id, "Так же слово Вайб используется в словосочитаниях ПЛЮС ВАЙБ и МИНУС ВАЙБ")
            bot.send_message(message.chat.id, "Минус вайб-ситуация огорчает,ухудшается общее эмоциональное состояние")
            bot.send_message(message.chat.id, "Плюс вайб-настроение поднимается,ситуация порадовала")
        elif message.text == "Имба" or message.text == "Имбовый" or message.text == "Имбища":
            bot.send_message(message.chat.id, opred.imba)
            bot.send_message(message.chat.id, "Пример:")
            bot.send_message(message.chat.id, primer.imbapr)
        elif message.text == "Криповый":
            bot.send_message(message.chat.id, opred.krip)
            bot.send_message(message.chat.id, "Пример:")
            bot.send_message(message.chat.id, primer.krippr)
        elif message.text == "Лейм":
            bot.send_message(message.chat.id, opred.lim)
            bot.send_message(message.chat.id, "Пример:")
            bot.send_message(message.chat.id, primer.limpr)
        elif message.text == "Сас" or message.text == "Сасный":
            bot.send_message(message.chat.id, opred.sas)
            bot.send_message(message.chat.id, "Пример:")
            bot.send_message(message.chat.id, primer.saspr)
        elif message.text == "Шеймить":
            bot.send_message(message.chat.id, opred.shim)
            bot.send_message(message.chat.id, "Пример:")
            bot.send_message(message.chat.id, primer.shimpr)
        elif message.text == "Шипперить" or message.text == "Шип" or message.text == "Шипирить" or message.text == "Шипп":
           bot.send_message(message.chat.id, opred.ship)
           bot.send_message(message.chat.id, "Пример:")
           bot.send_message(message.chat.id, primer.shippr)
        elif message.text == "Чиллить" or message.text == "Чилить" or message.text == "Чилл" or message.text == "Чил":
            bot.send_message(message.chat.id, opred.chill)
            bot.send_message(message.chat.id, "Пример:")
            bot.send_message(message.chat.id, primer.chillpr)
        elif message.text == "Байтить":
            bot.send_message(message.chat.id, opred.bait)
            bot.send_message(message.chat.id, "Пример:")
            bot.send_message(message.chat.id, primer.baitpr)
        elif message.text == "Форсить":
            bot.send_message(message.chat.id, opred.fors)
            bot.send_message(message.chat.id, "Пример:")
            bot.send_message(message.chat.id, primer.forpr)
        elif message.text == "Варик":
            bot.send_message(message.chat.id, opred.varic)
            bot.send_message(message.chat.id, "Пример:")
            bot.send_message(message.chat.id, primer.varicpr)
        elif message.text == "Душнила" or message.text == "Душный":
            bot.send_message(message.chat.id, opred.dush)
            bot.send_message(message.chat.id, "Пример:")
            bot.send_message(message.chat.id, primer.dushpr)
        elif message.text == "Жиза":
            bot.send_message(message.chat.id, opred.jiza)
        elif message.text == "Задрот":
            bot.send_message(message.chat.id, opred.zadrot)
            bot.send_message(message.chat.id, "Пример:")
            bot.send_message(message.chat.id, primer.zadrotpr)
        elif message.text == "Кринж" or message.text == "Кринжовый" or message.text == "Кринжевать" :
            bot.send_message(message.chat.id, opred.kringe)
            bot.send_message(message.chat.id, "Пример:")
            bot.send_message(message.chat.id, primer.kringepr)
        elif message.text == "Запилить":
            bot.send_message(message.chat.id, opred.pil)
            bot.send_message(message.chat.id, "Пример:")
            bot.send_message(message.chat.id, primer.pilpr)
        elif message.text == "Пруфы":
            bot.send_message(message.chat.id, opred.pruf)
            bot.send_message(message.chat.id, "Пример:")
            bot.send_message(message.chat.id, primer.prufpr)
        elif message.text == "Чекать":
            bot.send_message(message.chat.id, opred.chec)
            bot.send_message(message.chat.id, "Пример:")
            bot.send_message(message.chat.id, primer.checpr)
        elif message.text == "Читер":
            bot.send_message(message.chat.id, opred.chiter)
            bot.send_message(message.chat.id, "Пример:")
            bot.send_message(message.chat.id, primer.chiterpr)
        elif message.text == "ЧСВ":
            bot.send_message(message.chat.id, opred.csv)
            bot.send_message(message.chat.id, "Пример:")
            bot.send_message(message.chat.id, primer.csvpr)
        elif message.text == "Мем":
            bot.send_message(message.chat.id, opred.mem)
            bot.send_message(message.chat.id, "Пример:")
            bot.send_message(message.chat.id, primer.mempr)
        elif message.text == "Фрик":
            bot.send_message(message.chat.id, opred.frik)
            bot.send_message(message.chat.id, "Пример:")
            bot.send_message(message.chat.id, primer.fricpr)
        elif message.text == "Альтушка":
            bot.send_message(message.chat.id, opred.alit)
            bot.send_message(message.chat.id, "Пример:")
            bot.send_message(message.chat.id, primer.alitpr)
        elif message.text == "Муд":
            bot.send_message(message.chat.id, opred.mud)
        elif message.text == "Донатить" or message.text == "Донат":
            bot.send_message(message.chat.id, opred.donation)
            bot.send_message(message.chat.id, "Пример:")
            bot.send_message(message.chat.id, primer.donpr)
        elif message.text == "Зашквар" or message.text == "Зашкварный":
            bot.send_message(message.chat.id, opred.zashkvar)
            bot.send_message(message.chat.id, "Пример:")
            bot.send_message(message.chat.id, primer.zashkvarpr)
        elif message.text == "Зумер":
            bot.send_message(message.chat.id, opred.zum)
        elif message.text == "Пушка":
            bot.send_message(message.chat.id, opred.push)
        elif message.text == "Рак":
            bot.send_message(message.chat.id, opred.rak)
        elif message.text == "Рандом" or message.text == "Рандомный":
            bot.send_message(message.chat.id, opred.rand)
            bot.send_message(message.chat.id, "Пример:")
            bot.send_message(message.chat.id, primer.randpr)
        elif message.text == "Хейтер" or message.text == "Хейтерить":
            bot.send_message(message.chat.id, opred.heit)
            bot.send_message(message.chat.id, "Пример:")
            bot.send_message(message.chat.id, primer.heitpr)
        elif message.text == "Ивейтить":
            bot.send_message(message.chat.id, opred.invate)
        elif message.text == "ЛС":
            bot.send_message(message.chat.id, opred.ls)
            bot.send_message(message.chat.id, "Пример:")
            bot.send_message(message.chat.id, primer.lspr)
        elif message.text == "Мерч" or message.text == "Мерчовка":
            bot.send_message(message.chat.id, opred.merch)
            bot.send_message(message.chat.id, "Пример:")
            bot.send_message(message.chat.id, primer.merchpr)
        elif message.text == "Мьют":
            bot.send_message(message.chat.id, opred.mut)
            bot.send_message(message.chat.id, "Пример:")
            bot.send_message(message.chat.id, primer.mutpr)
        elif message.text == "Рофл" or message.text == "Рофлить" or message.text == "Рофельный":
            bot.send_message(message.chat.id, opred.rofl)
            bot.send_message(message.chat.id, "Пример:")
            bot.send_message(message.chat.id, primer.roflpr)
        elif message.text == "Сигма":
            bot.send_message(message.chat.id, opred.sigma)
        elif message.text == "Стэнить":
            bot.send_message(message.chat.id, opred.stem)
        elif message.text == "Тейк":
            bot.send_message(message.chat.id, opred.ttik)
        elif message.text == "Топ" or message.text == "Топовый":
            bot.send_message(message.chat.id, opred.top)
        elif message.text == "Треш" or message.text == "Трешовый":
            bot.send_message(message.chat.id, opred.tresh)
        elif message.text == "Ту мач":
            bot.send_message(message.chat.id, opred.tu)
        elif message.text == "Фича":
            bot.send_message(message.chat.id, opred.ficha)
        elif message.text == "Шарить":
            bot.send_message(message.chat.id, opred.shar)
        else:
            bot.send_message(message.chat.id, "К сожалению, я не знаю данного слова.")

bot.polling(none_stop=True)

