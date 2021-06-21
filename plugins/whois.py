#!/usr/bin/python
# -*- coding: utf8 -*-

import requests
from config import bot
from plugins.error import in_chat
from config import HEADERS
from telebot import types


@in_chat()
def whois(m):
    keyboard = types.InlineKeyboardMarkup()
    keyboard_delete = types.InlineKeyboardButton(text="❌",
                                                 callback_data="delete")
    keyboard.add(keyboard_delete)
    bot.delete_message(m.chat.id, m.message_id)

    ip = str(m.text[6:])
    get = requests.get(f"https://ipinfo.io/{ip}/json", headers=HEADERS)
    get = get.json()

    list_first = []
    list_double = []

    for line in get:
        list_first.append(line)

    for line in get:
        list_double.append(get[line])
    full = []
    list_double = list(map(str, list_double))

    try:
        if "bogon" in list_first:
            full = ip + "\nЭто локальный ip"
        else:
            for line in list(zip(list_first, list_double)):
                full.append(" ".join(line))

            if "status" in get:
                raise AttributeError

            full = "\n".join(full)
    except Exception:
        full = f"*{ip}* - не корректен"

    bot.send_message(m.chat.id,
                     text=f"*{full}*",
                     reply_markup=keyboard,
                     parse_mode="Markdown")
