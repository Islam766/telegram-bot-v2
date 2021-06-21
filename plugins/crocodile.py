#!/usr/bin/python
# -*- coding: utf8 -*-

from telebot import types
import random
from config import bot
from itertools import islice
from plugins.error import in_chat


@in_chat()
def crocodile(m):
    bot.delete_message(m.chat.id, m.message_id)
    crocodile.__annotations__["who_start"] = m.from_user.id
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text='Узнать слово',
                                        callback_data='word')
    button2 = types.InlineKeyboardButton(
                                    text="Новое слово",
                                    callback_data=f"new_word&&{m.from_user.id}"
                                    )
    markup.add(button)
    markup.add(button2)
    bot.send_message(chat_id=m.chat.id,
                     text=f'*{m.from_user.first_name}* _объясняет слово_',
                     reply_markup=markup,
                     parse_mode="Markdown")
    line = random.randint(1, 125853)

    with open('plugins/singular_and_plural.txt') as f:
        word_txt = next(islice(f, line, None))

    crocodile.__annotations__['word_txt'] = word_txt


def new_crocodile(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)
    user_id = call.data.split("&&")[1]
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text='Узнать слово',
                                        callback_data='word')
    button2 = types.InlineKeyboardButton(
                                text="Новое слово",
                                callback_data=f"new_word&&{call.from_user.id}")
    markup.add(button)
    markup.add(button2)
    bot.send_message(chat_id=call.message.chat.id,
                     text=f'*{call.from_user.first_name}* _объясняет слово_',
                     reply_markup=markup,
                     parse_mode="Markdown")
    line = random.randint(1, 125853)

    with open('plugins/singular_and_plural.txt') as f:
        word_txt = next(islice(f, line, None))

    crocodile.__annotations__['word_txt'] = word_txt


def crocodile_win(m):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(
                        text="Стать ведущим!",
                        callback_data=f"new_crocodile&&{m.from_user.id}")
    keyboard_delete = types.InlineKeyboardButton(text="❌",
                                                 callback_data="delete")
    markup.add(button, keyboard_delete)
    bot.send_message(chat_id=m.chat.id,
                     text=f"*{m.from_user.first_name}* _угадал(a) слово_!",
                     reply_markup=markup,
                     parse_mode="Markdown")

crocodile.__annotations__['word_txt'] = "$%^&*None*&^%$#"
