#!/usr/bin/python
# -*- coding: utf8 -*-


from config import bot
from translate import Translator
from plugins.error import Error
from plugins.error import in_chat


@in_chat()
def ru(m):
    """ Перевод на русский """
    bot.delete_message(m.chat.id, m.message_id)
    try:
        translator = Translator(to_lang="ru", from_lang="en")
        translation = translator.translate(m.text[4:])
        bot.send_message(m.chat.id, "Перевод: " + translation)
    except:
        Error(m, bot).error()


@in_chat()
def en(m):
    """ Перевод на английский """
    bot.delete_message(m.chat.id, m.message_id)
    try:
        translator = Translator(to_lang="en", from_lang="ru")
        translation = translator.translate(m.text[4:])
        bot.send_message(m.chat.id, "Перевод: " + translation)
    except:
        Error(m, bot).error()
