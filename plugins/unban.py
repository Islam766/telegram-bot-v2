#!/usr/bin/python
# -*- coding: utf8 -*-


from config import bot
from plugins.error import in_chat
from plugins.error import check_admin
import time


@in_chat()
@check_admin()
def unban(m):
    bot.delete_message(m.chat.id, m.message_id)
    try:
        user_id = str(m.reply_to_message.from_user.id)
    except:
        pass

    if len(user_id) == 9 or len(user_id) == 10:
        bot.unban_chat_member("-1001293845658",
                                user_id,
                                only_if_banned=True)
    else:
        bot.send_message(m.chat.id,
                            f"*Увы, user_id {user_id} неверен*",
                            parse_mode="Markdown")
        time.sleep(5)
        bot.delete_message(m.chat.id, m.message_id + 1)
