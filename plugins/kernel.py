#!/usr/bin/python
# -*- coding: utf8 -*-

from config import bot
from config import HEADERS
from plugins.error import in_chat
import requests
from bs4 import BeautifulSoup as bs
from telebot import types

@in_chat()
def kernel(m):
    try:
        keyboard = types.InlineKeyboardMarkup()
        keyboard_delete = types.InlineKeyboardButton(text = "❌", callback_data = "delete")
        keyboard.add(keyboard_delete)

        bot.delete_message(m.chat.id, m.message_id) #

        ##############################################################
        # kernel: запрос/группировка данных
        res = requests.get("https://kernel.org", headers = HEADERS)
        html = bs(res.text, "lxml")   # Запрос и получаем html

        versions = html.select("td strong")[1:]
        names = html.select("td")         # Ищем теги
        dates = html.select("td:nth-of-type(3)")
        links = html.select("a[title='Download complete tarball']")

        names_list = []
        versions_list = []           # Списки, некоторые нам понадобятся в будущем
        sort_names_list = []
        sort_date_list = []
        sort_links_list = []

        for line in versions:
            versions_list.append(line.get_text())     # Получаем список с версиями ядра

        for line in names:
            names_list.append(line.get_text())         # Получаем смешанный список с названием и ссылями

        for line in names_list:
            if ":" in line:
                sort_names_list.append(line)           # Убираем все ненужное, отделяем ссылки
        sort_names_list = sort_names_list[3:]

        for line in links:
            sort_links_list.append(line.get("href"))  # Получаем ссылки

        for line in dates:
            sort_date_list.append(line.get_text())     # Получаем даты, без всякой херни
        full_info = list(zip(sort_names_list, versions_list, sort_date_list, sort_links_list))
        ##############################################################

        R = full_info
        full_info = []
        full_info_2 = []

        for line in R:
            for line_2 in line:
                if line_2 == line[3]: pass
                elif len(line_2) == 10:
                    full_info.append("[{}]({})\n".format(line_2, line[3]))
                else:
                    full_info.append("[{}]({})".format(line_2, line[3]))

        for line in full_info:
            if "[EOL]" in line:
                eol = line.replace(" ", "")
                eol = eol.replace("[EOL]", " | EOL |")
                full_info_2.append(eol)
            else:
                full_info_2.append(line)
        full_info_2 = "  ".join(full_info_2) #
        bot.send_message(m.chat.id, text ="*Версии ядер: \n\n*" + full_info_2, reply_markup = keyboard, parse_mode = "Markdown")
############################################################################################
    except Exception as e:
        print ("kernel.py ", end = "")
        print (f"❌❌❌❌❌{e} ❌❌❌❌❌")
