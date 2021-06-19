#!/usr/bin/python
# -*- coding: utf8 -*-

from telebot import ApiTelegramException
from config import bot
from time import sleep
from plugins.error import (in_chat,
                           check_reply,
                           check_admin,
                           check_private)


@in_chat()
@check_admin()
@check_private()
@check_reply()
def pin(m):
    """ Команда /pin закрепить сообщение """
    bot.delete_message(m.chat.id, m.message_id)
    bot.pin_chat_message(m.chat.id, m.reply_to_message.message_id)
    sent = bot.send_message(m.chat.id, "Сообщение успешно закреплено!")
    sleep(10)
    bot.delete_message(m.chat.id, sent.message_id)


@check_admin()
@in_chat()
@check_private()
def unpin(m):
    """ Команда /unpin открепить сообщение """
    bot.delete_message(m.chat.id, m.message_id)
    try:
        bot.unpin_chat_message(m.chat.id)
        sent = bot.send_message(m.chat.id, "Сообщение успешно откреплено!")
        sleep(10)
        bot.delete_message(m.chat.id, sent.message_id)
    except ApiTelegramException:
        delete = bot.send_message(m.chat.id, "Нечего откреплять!")
        sleep(5)
        bot.delete_message(m.chat.id, delete.message_id)
