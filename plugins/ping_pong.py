#!/usr/bin/python
# -*- coding: utf8 -*-

from config import bot
import datetime
import psutil
from telebot import types
import warnings
from plugins.error import in_chat
from config import version

warnings.filterwarnings("ignore")


def date_start():
    """ Начало работы бота """
    date_start.__annotations__["time_start"] = datetime.datetime.now()


@in_chat()
def ping(m):
    bot.delete_message(m.chat.id, m.message_id)

    keyboard = types.InlineKeyboardMarkup()
    keyboard_delete = types.InlineKeyboardButton(text="❌",
                                                    callback_data="delete")
    keyboard.add(keyboard_delete)
    now = datetime.datetime.now()
    work_bot = now - date_start.__annotations__["time_start"]

    seconds = work_bot.seconds

    if seconds > 60:
        time = float(seconds) / 60   # Перевод в минуты
        what_time = "минут"
        if time > 60:
            time = float(time) / 60        # Перевод в часы
            what_time = "часов"
            if time > 24:
                time = float(time) / 24
                what_time = "дней"
    else:                         # В случае, если переводить ненужно
        time = seconds
        what_time = "секунд"

    find = str(time).find(".") + 3
    time = str(time)[:find]
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent

    bot.send_message(m.chat.id,
                        text=f"*PONG*🏓\n\n_Время работы бота_: "
                        f"*{round (float(time), 2)}* *{what_time}*"
                        f"\n_Версия бота_: *{version}*"
                        "\n\n_Информация сервера_:"
                        f"\n_CPU_: *{cpu}%*\n_MEM_: *{mem}%*",

                        parse_mode="Markdown",
                        reply_markup=keyboard)

