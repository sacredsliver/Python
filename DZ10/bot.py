import telebot
from telebot import types
import model as md
import controller as con

TOKEN = ""
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['db'])
def start_db(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    rec_all = types.KeyboardButton('Показать все записи справочника')
    rec_add = types.KeyboardButton('Добавить запись')
    rec_del = types.KeyboardButton('Удалить запись')
    rec_edit = types.KeyboardButton('Изменить запись')
    db_close = types.KeyboardButton('Завершить работу с БД')
    markup.add(rec_all, rec_add, rec_del, rec_edit, db_close)
    bot.send_message(message.chat.id, '{0.first_name} ,добро пожаловать в БД'.format(
        message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    db = con.open_db()
    if message.text == 'Показать все записи справочника':
        for k, v in db.items():
            bot.send_message(message.chat.id, str(k) + ' ' + v)
    elif message.text == 'Добавить запись':
        bot.send_message(message.chat.id, 'Введите данные для добавления....')
        bot.register_next_step_handler(message, add_rec)
    elif message.text == 'Удалить запись':
        bot.send_message(message.chat.id, 'Введите номер записи для удаления....')
        bot.register_next_step_handler(message, del_rec)
    elif message.text == 'Изменить запись':
        bot.send_message(message.chat.id, 'Введите номер записи для изменения и новое значение через тире '
                                          '(например 4-Антонов Павел Максимович глав.бух уволен')
        bot.register_next_step_handler(message, edit_rec)
    elif message.text == 'Завершить работу с БД':
        markup = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Работы с БД завершена', reply_markup=markup)


def add_rec(message):
    text = message.text
    md.add(text)


def del_rec(message):
    text = message.text
    md.del_value(text)


def edit_rec(message):
    text = message.text
    md.edit_value(text)


bot.polling()
