#!/usr/bin/python
# -*- coding: utf8 -*-

from config import bot, HEADERS
from telebot import types
import requests
from bs4 import BeautifulSoup
from plugins.error import in_chat


@in_chat()
def cats(m):
    bot.delete_message(m.chat.id, m.message_id)
    keyboard = types.InlineKeyboardMarkup()  # Добавляем кнопки
    cats = types.InlineKeyboardButton(text="Еще хочу котейку",
                                      callback_data="cats")
    keyboard.add(cats)  # Добавляем кнопки для вывода

    search = "https://theoldreader.com/kittens/1366/768/js"
    # Запрашиваем у юзера, что он хочет найти
    url = requests.get(search, headers=HEADERS)  # Делаем запрос
    soup = BeautifulSoup(url.text, features="lxml")  # Получаем запрос
    result = soup.find("img").get("src")  # Ищем тег <img src="ссылка.png"
    result = "https://theoldreader.com" + result
    bot.send_photo(m.chat.id, photo=result,
                   reply_markup=keyboard,
                   parse_mode="Markdown")
