#!/usr/bin/python
# -*- coding: utf8 -*-

from config import bot
from time import sleep
from plugins.error import in_chat


@in_chat()
def github(m):
    """ Команда /github моя ветка на гитхабе """
    bot.delete_message(m.chat.id, m.message_id)
    delete=bot.send_message(
        m.chat.id,
        "_Репозиторий кота_ [Тык](https://"
        "github.com/evilcatsystem)\n"
                                        "_Активный репозиторий _[Тык]"
                                        "(https://github.com/angry-kitty-linux/telegram-bot-v2)"
            , parse_mode= "Markdown") #Отправляем сообщение
    sleep(10)
    bot.delete_message(m.chat.id, delete.message_id)
