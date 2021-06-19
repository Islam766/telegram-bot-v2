#!/usr/bin/python
# -*- coding: utf8 -*-

import requests
from bs4 import BeautifulSoup
from config import bot
import telebot.types as types
from plugins.error import in_chat
from config import HEADERS


@in_chat()
def news(m):
    bot.delete_message(m.chat.id, m.message_id)
    keyboard = types.InlineKeyboardMarkup()
    keyboard_delete = types.InlineKeyboardButton(text="❌",
                                                 callback_data="delete")
    keyboard.add(keyboard_delete)

    url = requests.get('https://www.opennet.ru/#', headers=HEADERS)
    soup = BeautifulSoup(url.text, features="lxml")

    tags = soup.find_all('td', class_="tnews")
    results_news = []
    for b in tags:
        url = b.find('a').get('href')
        title = b.find('a').text
        results = f'<a href="https://www.opennet.ru{url}">{title}</a>'
        results_news.append(results)
        results_lists_news = "\n".join(results_news)
    bot.send_message(m.chat.id,
                     "\n🆕 Новости 🆕\n" + results_lists_news,
                     reply_markup=keyboard,
                     disable_web_page_preview=True,
                     parse_mode="HTML")
