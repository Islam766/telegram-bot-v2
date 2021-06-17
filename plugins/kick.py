#!/usr/bin/python
# -*- coding: utf8 -*-

from config import bot
from plugins.error import Error
from plugins.error import (in_chat,
                           check_reply,
                           check_private,
                           check_admin,
                           check_exist_user)


@in_chat()
@check_private()
@check_admin()
@check_reply()
@check_exist_user()
def kick(m):
    bot.delete_message(m.chat.id, m.message_id)
    bool_ = Error(m, bot).check_reply_admin_()
    if m.reply_to_message.from_user.id == 905933085:
        bot.send_message(
            m.chat.id, f"*{m.from_user.first_name}*, по голове постучи себе!",
            parse_mode="Markdown")
    elif bool_ is True:
        bot.kick_chat_member(m.chat.id,
                             m.reply_to_message.from_user.id)  # Удаляем
    elif bool_ is False:
        Error(m, bot).message_admin()
