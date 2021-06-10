#!/usr/bin/python
# -*- coding: utf8 -*-

""" Работа второго бота, создан для перезагрузки основного """

from telebot import types
import telebot
from telebot import apihelper

from urllib3.connectionpool import InsecureRequestWarning

import warnings

from config import token2
from config import app
from config import id_s

from plugins.error import *

try:
    ###############################################
    # Игнорирование варнингов
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    warnings.filterwarnings("ignore", category=InsecureRequestWarning)
    ##############################################

    keyboard = types.InlineKeyboardMarkup()
    keyboard_delete = types.InlineKeyboardButton(text="❌",
                                                 callback_data="delete")
    keyboard.add(keyboard_delete)

    print(open("banner", "r").read())  # Баннер

    token = token2
    bot = telebot.TeleBot(token, threaded=True)


    def restart_(m, autorestart: bool = False):
        """ Перезапуск бота """
        try:
            if autorestart is True:  # Принудительная перезагрузка
                app.restart()
            else:

                if (m.from_user.id in id_s) is False:
                    bot.delete_message(m.chat.id, m.message_id)

                    bot.send_message(m.chat.id, 
                        """
                        *Данная команда доступна:*
                        \n 1. Opelsin
                        \n 2. No such file or directory [АПАСНАЯ КАТЯРА]
                        \n 3. 7F673F4B1A🕷
                        \n 4. Evil Cat Чек Профиль
                        \n 5. recursive_cat
                        """, reply_markup=keyboard, parse_mode="Markdown")

                else:
                    try:
                        app.restart()
                        bot.send_message(905933085,
                                         "*Все боты будут перезапущены через 5"
                                         "секунд!*", 
                                         parse_mode="Markdown")
                    except:
                        Error(m, bot).error()
        except (Exception, apihelper.ApiTelegramException) as e:
            print("manage.py | restart_ ", end="")
            print(f"❌❌❌❌❌{e} ❌❌❌❌❌")

    def autorestart__(m):
        """ Авторестарт """
        try:
            logs = (app.get_log(lines=20)).split("\n")
            bools = ["Process exited with status 0" in str(line)
                     for line in logs]

            bools_2 = ["Traceback (most recent call last):" in str(line)
                       for line in logs]

            bools_3 = ["line" in str(line)
                       for line in logs]

            if True in bools or True in bools_2 or True in bools_3:
                print("❌❌❌❌❌ Ошибка обнаружена! Перезапускаю... ❌❌❌❌❌")
                restart_(m, autorestart=True)
        except (Exception, apihelper.ApiTelegramException) as e:
            print("manage.py | autorestart__ ", end="")
            print(f"❌❌❌❌❌{e} ❌❌❌❌❌")

    @bot.message_handler(commands=["restart"])
    def restart(m):
        restart_(m)

    @bot.message_handler(func=lambda message: True, content_types=["text", "sticker", "photo", "audio", "video", "document"])
    def autorestart(m):
        autorestart__(m)




    bot.polling()
except (Exception, apihelper.ApiTelegramException) as e:
   print (e)
