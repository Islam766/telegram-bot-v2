#!/usr/bin/python
##################################################################
try: 
    # Внутренние конфиги 
    from config import heroku_conn
    from config import chat_id        
    from config import HEADERS
    from config import token2
    from config import conn
    from config import app

    from plugins.error import *
    ######################################################
    # Телеграмовские библиотеки
    from telebot import types
    import telebot
    from telebot import apihelper
    ######################################################
    # Варнинги
    from urllib3.connectionpool import InsecureRequestWarning
    import warnings
    ######################################################
    # Хероку
    import heroku3
    from config import app
    ###############################################
    # Игнорирование варнингов
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    warnings.filterwarnings("ignore", category=InsecureRequestWarning)
    ##############################################

    keyboard = types.InlineKeyboardMarkup()
    keyboard_delete = types.InlineKeyboardButton(text = "❌", callback_data = "delete")
    keyboard.add(keyboard_delete)

    print (open("banner", "r").read())                  # Баннер

    token = token2
    bot = telebot.TeleBot(token, threaded=True)


    def restart_ (m, autorestart = False):
        try:
            if autorestart is True:
                app.restart()
            else:

                id_s = ['<пользователи кототые могут ввести /restart>']

                if (m.from_user.id in id_s) is False:
                    bot.delete_message(m.chat.id, m.message_id)

                    bot.send_message(m.chat.id, """
                        *Данная команда доступна:*
                        \n 1. * 
                        \n 2. *
                        \n 3. *
                        \n 4. *
                        \n 5. *
                        """,
                            reply_markup = keyboard, parse_mode = "Markdown")

                else:
                    try:
                        app.restart()
                    except:
                        Error(m, bot).error()
        except (Exception, apihelper.ApiTelegramException) as e:
            print ("manage.py | restart_ ", end = "")
            print (f"❌❌❌❌❌{e} ❌❌❌❌❌")

    def autorestart__(m):
        try:
            logs = (app.get_log(lines = 20)).split("\n")        ##

            bools = ["Process exited with status 0" in str(line) for line in logs]
            bools_2 = ["Traceback (most recent call last):" in str(line) for line in logs]
            bools_3 = ["line" in str(line) for line in logs]
            if True in bools or True in bools_2 or True in bools_3:
                print ("❌❌❌❌❌ Ошибка обнаружена! Перезапускаю... ❌❌❌❌❌")
                restart_(m, autorestart = True) #
        except (Exception, apihelper.ApiTelegramException) as e:
            print ("manage.py | autorestart__ ", end = "")
            print (f"❌❌❌❌❌{e} ❌❌❌❌❌")

    @bot.message_handler(commands=["restart"])
    def restart(m):
        restart_(m)

    @bot.message_handler(func=lambda message: True, content_types=["text", "sticker", "photo", "audio", "video", "document"])
    def autorestart(m):
        autorestart__(m)


    bot.polling()
except (Exception, apihelper.ApiTelegramException) as e:
   print (e)
