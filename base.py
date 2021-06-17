#!/usr/bin/python
# -*- coding: utf8 -*-

import base64
from config import bot, chat_id
from plugins.error import Error
from plugins.log_error import logfile
from plugins.error import in_chat


@in_chat()
def encode(message):
    """ Кодируем в base64 """
    bot.delete_message(message.chat.id, message.message_id)
    repeat = bot.send_message(message.chat.id, "***")

    message_text = message.text[7:]
    encode_message = message_text.encode("UTF-8")
    encode_text = base64.b64encode(encode_message)
    bot.edit_message_text(chat_id=message.chat.id,
                          text=encode_text,
                          message_id=repeat.message_id)


@in_chat()
def decode(message):
    """ Декодируем base64 """
    bot.delete_message(message.chat.id, message.message_id)
    repeat = bot.send_message(message.chat.id, "***")
    message_text = message.text[7:]
    encode_message = message_text.encode("UTF-8")
    decode_text = base64.b64decode(encode_message)
    bot.edit_message_text(chat_id=message.chat.id,
                          text=decode_text,
                          message_id=repeat.message_id)
