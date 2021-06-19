#!/usr/bin/python
# -*- coding: utf8 -*-

""" Создание скриншота сайта """

from config import bot, chat_id
from plugins.error import Error
import requests
from bs4 import BeautifulSoup
import time
from telebot import types
from plugins.error import in_chat
from config import HEADERS


@bot.message_handler(commands=['url'])
@in_chat()
def screen(m):
    bot.delete_message(m.chat.id, m.message_id)
    keyboard = types.InlineKeyboardMarkup()
    keyboard_delete = types.InlineKeyboardButton(text="❌",
                                                 callback_data="delete")
    keyboard.add(keyboard_delete)

    link = m.text[5:]

    if not link.startswith(("https://", "http://")):
        link = f"https://{link}"

    html = requests.get(link, headers=HEADERS).text

    # Защита от спермотоксикозников
    bool_ = ("Порн" in html
             or "Porn" in html
             or "porn" in html
             or "порн" in html)

    if bool_ is True:
        bot.send_sticker(m.chat.id,
                         "CAACAgQAAxkBAAIaSF93cwIsw1oPRGtOdZHTF8_UsBTDAAJYAAO"
                         "6erwZr3-jVb-xFsgbBA")
        time.sleep(15.5)
        bot.delete_message(m.chat.id, m.message_id + 1)
    else:
        photo = "https://mini.s-shot.ru/1366x768/JPEG/1366/Z100/?" + link
        bot.send_photo(m.chat.id, photo, reply_markup=keyboard)
