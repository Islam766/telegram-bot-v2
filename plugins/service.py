#!/usr/bin/python
# -*- coding: utf8 -*-


from config import bot, chat_id, user_id, conn
import datetime
from plugins.top import writes


def handler_new_member(m):
    """ Встречаем нового пользователя в чате """
    bot.delete_message(m.chat.id, m.message_id)
    id = m.json
    id = id['new_chat_members']
    for a in id:
        id = a['id']
        name = a['first_name']
    last = f'<a href="tg://user?id={id}">{name}</a>'
    bot.send_sticker(m.chat.id, "CAACAgIAAxkBAAJFW16Tj7HCIcjx9fPTf3WYtEXLG4EJA"
                     "AIDAAOF-3IqNguusCQT_gEYBA")  # Отправить стикер
    bot.send_message(m.chat.id, f"Добро пожаловать, {last} \nНапиши /help, что"
                     "бы мной воспользоваться", parse_mode="HTML")
    bot.export_chat_invite_link(chat_id)

    #######################################################
    writes(m)
    cursor = conn.cursor()
    cursor.execute("UPDATE top_users SET date_add = '{date}'"
                   "WHERE user_id = {m.from_user.id};")
    conn.commit()
    ########################################################


def left_chat_member(m):
    """ Провожаем вышедшего пользователя """
    try:
        bot.delete_message(m.chat.id, m.message_id)
        bot.export_chat_invite_link(chat_id)
        first = '<a href="tg://user?id='
        f'{m.from_user.id}">{m.from_user.first_name}</a>'
        last = '<a href="tg://user?id='
        f'{m.left_chat_member.id}">{m.left_chat_member.first_name}</a>'
        if m.from_user.id != m.left_chat_member.id:
            bot.send_sticker(m.chat.id, 'CAACAgIAAxkBAAJMe1-lM12m7DQqSelOfsAs3'
                             'qzBZbY7AAKPEQACPLPFBzLcyrxNSGysHgQ')
            # Отправить стикер
            result = first + " кикнул(a) " + last
            bot.send_message(m.chat.id, result, parse_mode=('HTML'))
        else:
            bot.send_sticker(m.chat.id, 'CAACAgIAAxkBAAJMe1-lM12m7DQqSelOfsAs3'
                             'qzBZbY7AAKPEQACPLPFBzLcyrxNSGysHgQ')
            # Отправить стикер
            bot.send_message(m.chat.id, last + ' покинул(a) нас',
                             parse_mode=("HTML"))
            # Уведомляем, что пользователь вышел
        cursor = conn.cursor()
        userid = m.left_chat_member.id
        cursor.execute("DELETE FROM top_users"
                       " WHERE user_id = " + str(userid) + ";")
        conn.commit()
    except:
        bot.send_message(user_id, "Я - псих. И устал от вас, прощайте.")
