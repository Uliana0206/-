import telebot
from telebot import types


bot = telebot.TeleBot('8427573354:AAHb2MahdqL4C1zg7inxXeQ05xarMbLZxRk')

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
            bot.send_message(message.chat.id, "Список:Альтушка, Байтить, Вайб, Варик, Душнила, Жиза, Задрот, Запилить, Имба, Кринж, Криповый, Лейм, Мем, Мем, Пруфычекать, Сас, Форсить, Фрик, Чиллить, Читер, ЧСВ, Шеймить, Шипперить")
            bot.send_message(message.chat.id, "Введите интересующее вас слово с заглавной буквы")
        else:
            bot.send_message(message.chat.id, "Введите интересующее вас слово с заглавной буквы")


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == "Вайб" or message.text == "Плюс вайб" or message.text == "Минус вайб":
            bot.send_message(message.chat.id, "Вайб — атмосфера или настроение")
            bot.send_message(message.chat.id, "Так же слово Вайб используется в словосочитаниях ПЛЮС ВАЙБ и МИНУС ВАЙБ")
            bot.send_message(message.chat.id, "Минус вайб-ситуация огорчает,ухудшается общее эмоциональное состояние")
            bot.send_message(message.chat.id, "Плюс вайб-настроение поднимается,ситуация порадовала")
        elif message.text == "Имба":
            bot.send_message(message.chat.id, "Имба — мощный, выдающийся по характеристикам, круто, классно")
        elif message.text == "Криповый":
            bot.send_message(message.chat.id, "Криповый — очень страшный, вызывающий ужас")
        elif message.text == "Лейм":
            bot.send_message(message.chat.id, "Лейм — нечто скучное, банальное, унылое, скучный, неинтересный человек")
        elif message.text == "Сас" or message.text == "Сасный":
            bot.send_message(message.chat.id, "Сас, сасный — красивый, эффектный, притягательный, вызывающий влечение, сомнительный, подозрительный")
        elif message.text == "Шеймить":
            bot.send_message(message.chat.id, "Шеймить — пристыдить кого-либо")
        elif message.text == "Шипперить":
           bot.send_message(message.chat.id, "Шипперить — придумывать, что какие-то известные люди или персонажи состоят в романтических отношениях, хотя в действительности это не так")
        elif message.text == "Чиллить" or message.text == "Чилить" or message.text == "Чилл" or message.text == "Чил":
            bot.send_message(message.chat.id, "Чилить — отдыхать, расслабляться, приятно проводить время")
        elif message.text == "Байтить":
            bot.send_message(message.chat.id, "Байтить- приманивать,провоцировать")
        elif message.text == "Форсить":
            bot.send_message(message.chat.id, "Форсить — продвигать, популяризировать")
        elif message.text == "Варик":
            bot.send_message(message.chat.id, "Варик — вариант развития событий")
        elif message.text == "Душнила":
            bot.send_message(message.chat.id, "Душнила — скучный и нудный человек в компании, постоянно высказывающий непопулярное мнение")
        elif message.text == "Жиза":
            bot.send_message(message.chat.id, "Жиза — ситуация, актуальная для слушателя")
        elif message.text == "Задрот":
            bot.send_message(message.chat.id, "Задрот — человек, который много времени тратит на компьютерные игры")
        elif message.text == "Кринж":
            bot.send_message(message.chat.id, "Кринж - это стыд или смущение за действия и слова другого человека")
        elif message.text == "Запилить":
            bot.send_message(message.chat.id, 'Запилить — опубликовать определённое фото или видео в интернет')
        elif message.text == "Пруфы":
            bot.send_message(message.chat.id, 'Пруфы — доказательства')
        elif message.text == "Чекать":
            bot.send_message(message.chat.id, 'Чекать — проверять, смотреть')
        elif message.text == "Читер":
            bot.send_message(message.chat.id, 'Читер — человек, использующий жульнические приёмы в компьютерных или настольных играх или в жизни')
        elif message.text == "ЧСВ":
            bot.send_message(message.chat.id, 'ЧСВ — сокращение фразы «чувство собственной важности», как правило используется в значении «надменный»')
        elif message.text == "Мем":
            bot.send_message(message.chat.id, 'Мем — смешная картинка или видеоролик в интернете')
        elif message.text == "Фрик":
            bot.send_message(message.chat.id, 'Фрик — слово, которое обозначает странного или эксцентричного человека')
        elif message.text == "Альтушка":
            bot.send_message(message.chat.id, 'Альтушка - девушка,которая старается выделиться эпотажной внешностью и поведением')
        elif message.text == "Муд":
            bot.send_message(message.chat.id, 'Муд — настроение или состояние')
        else:
            bot.send_message(message.chat.id, "К сожалению, я не знаю данного слова.")




bot.polling(none_stop=True)
