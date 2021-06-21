#!/usr/bin/python
# -*- coding: utf8 -*-

from config import bot
import wikipediaapi
from time import sleep
from telebot import types
from plugins.error import in_chat


@in_chat()
def wikipedia(m):
    bot.delete_message(m.chat.id, m.message_id)
    wiki_wiki = wikipediaapi.Wikipedia(
                                language='ru',
                                extract_format=wikipediaapi.ExtractFormat.WIKI)
    page_py = wiki_wiki.page(m.text[6:])
    try:
        keyboard = types.InlineKeyboardMarkup()
        wiki = types.InlineKeyboardButton(text="Читать на Википедии",
                                          url=page_py.canonicalurl)

        delete = types.InlineKeyboardButton(text="❌",
                                            callback_data="delete")
        keyboard.add(wiki, delete)
        bot.send_message(m.chat.id, page_py.summary, reply_markup=keyboard)
    except:
        delete = bot.send_message(m.chat.id, m.text[6:] + " не найдено")
        sleep(5)
        bot.delete_message(m.chat.id, delete.message_id)
