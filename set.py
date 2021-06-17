#!/usr/bin/python

from plugins.check_root import check_root
from config import bot
from config import conn
import psycopg2

############################################################################################
# Изменение в таблицы счетчика
def set_(m):                           # Изменение значение в бд
    check = check_root(m)
    if check[0] == True:
        bot.delete_message(m.chat.id, m.message_id)
        try:
            int(m.reply_to_message.from_user.id)
        except:
            info = m.text[4:].split()
            cursor = check[2]
            conn = check[1]
            cursor.execute(f"UPDATE top_users SET message = {info[1]} WHERE user_id = {str(info[0])} ;")
            conn.commit()
        else:
            info = m.text.split()
            cursor = check[2]
            conn = check[1]
            cursor.execute(f"UPDATE top_users SET message = {str(info[1])} WHERE user_id = {str(m.reply_to_message.from_user.id)};")
            conn.commit()
############################################################################################
