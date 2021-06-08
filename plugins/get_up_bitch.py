#!/usr/bin/python

from config import bot
from plugins.error import check_admin
from plugins.error import in_chat
from plugins.error import check_reply

@in_chat()
@check_admin()
@check_reply()
def get_up(m):
    bot.delete_message(m.chat.id, m.message_id)
    bot.send_message(m.reply_to_message.from_user.id, "*Так-с. А ну быстро в чат! Прекращай в тихушку сидеть!*",
                     parse_mode = "Markdown")
