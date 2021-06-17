#!/usr/bin/python
# -*- coding: utf8 -*-


import pickle

import requests
from bs4 import BeautifulSoup as bs
from telebot import types
from telebot import apihelper

from plugins.error import in_chat
from config import bot
from config import HEADERS

###############################################################################
def send_callback_news(call, num):
    keyboard = types.InlineKeyboardMarkup()
    keyboard_delete = types.InlineKeyboardButton(text="❌",
                                                 callback_data="delete")
    keyboard_back = types.InlineKeyboardButton(text="🔙",
                                               callback_data="back")
    keyboard.add(keyboard_delete, keyboard_back)

    with open("plugins/.arch_news_info.pickle", "rb") as file:
        download = pickle.load(file)

    full_links_3 = ["https://archlinux.org.ru" + line
                    for line in download["links"]][:3]

    res = requests.get(full_links_3[num], headers=HEADERS)
    html = bs(res.text, "lxml")

    find_title = html.find("h1").get_text()  # Заголовок
    find_info = html.find("td",
                          {"class": "post-content"}
                          ).get_text()  # Получаем описание

    find_code = html.find("code")  # Получаем код
    find_end = html.find("div",
                         {"class": "post-signature"})  # Получаем цитату

    if find_code is None:     # В случае, если кода нет
        find_code = ""

    elif find_end is None:    # В случае, если нет цитаты
        find_end = ""
    else:      # Если всё есть
        find_code = find_code.get_text()
        find_end = find_end.get_text()

        find_info = find_info.replace(find_code,
                                      "\n\n`" + find_code + "`")
        find_info = find_info.replace(find_end, "")
        find_info = find_info.replace(".", ". ")
        find_info = find_info.replace(",", ", ")

    all_find = f"*{find_title}*\n\n _{find_info}_\n\n"

    try:
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text=str(all_find),
                              reply_markup=keyboard,
                              parse_mode="Markdown")
    except apihelper.ApiTelegramException:
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text=str(all_find),
                              reply_markup=keyboard,
                              parse_mode="html")


@in_chat()
def arch__news(m):
    keyboard = types.InlineKeyboardMarkup()
    keyboard_delete = types.InlineKeyboardButton(text="❌",
                                                 callback_data="delete")
    keyboard.add(keyboard_delete)

    bot.delete_message(m.chat.id, m.message_id)
    res = requests.get("https://archlinux.org.ru/news/", headers=HEADERS)
    html = bs(res.text, "lxml")
    find = html.find_all("div",
                         {"class": "block"})

    titles = []
    links = []
    full_links = []
    full = []         # Списки, некоторые нам пригодятся позже

    for line in find:    # Заголовки
        find_info = line.find("a").get_text()
        titles.append(find_info)

    for line in find:   # Получаем ссыли
        find_info = line.find("a").get("href")
        links.append(find_info)

    full_links = ["https://archlinux.org.ru" + line for line in links]

    for line in range(3):  # Превращаем обычный текст в ссыль
        full.append("[{0}]({1})".format(titles[line], full_links[line]))

    titles = titles[3:]

    keyboard = types.InlineKeyboardMarkup()
    keyboard_delete = types.InlineKeyboardButton(text="❌",
                                                 callback_data="delete")

    keyboard_one = types.InlineKeyboardButton(text="1⃣",
                                              callback_data="b_zero")

    keyboard_two = types.InlineKeyboardButton(text="2⃣",
                                              callback_data="b_one")

    keyboard_tree = types.InlineKeyboardButton(text="3⃣",
                                               callback_data="b_two")

    keyboard_next = types.InlineKeyboardButton(text="🔜",
                                               callback_data="next")

    keyboard.add(keyboard_one,
                 keyboard_two,
                 keyboard_tree,
                 keyboard_delete,
                 keyboard_next
                 )

    bot.send_message(m.chat.id, "*Новости арча* \n\n" + "\n\n".join(full),
                     reply_markup=keyboard, parse_mode="Markdown")

    with open("plugins/.arch_news_info.pickle", "wb") as file:
        pickle.dump({
            "titles": titles,
            "links": links
        }, file)
