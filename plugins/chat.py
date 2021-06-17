#!/usr/bin/python
# -*- coding: utf8 -*-

from config import bot, chat_id, group_id
from time import sleep
from plugins.error import Error
from plugins.error import in_chat, check_reply, check_admin
from telebot import apihelper


@in_chat()
def id_chat(m):
    """ Получить айди чата, если не знаете айди, то закомментируйте строки
    @in_chat с проверкой пользователя на наличие его в чате
    """

    bot.delete_message(m.chat.id, m.message_id)
    bot.send_message(m.chat.id,
                     "Айди чата " + m.chat.title + ": " + str(m.chat.id))


@in_chat()
@check_admin()
def description(m):
    """ Меняем описание чата """
    bot.delete_message(m.chat.id, m.message_id)
    try:
        bot.set_chat_description(chat_id, m.text[5:])
        sent = bot.send_message(m.chat.id,
                                "Описание чата изменено на: " + m.text[5:])
        sleep(10)
        bot.delete_message(m.chat.id, sent.message_id)
    except Exception:
        Error(m, bot).error()


@in_chat()
@check_admin()
def link(m):
    """ Получаем ссылку на приглашение в чат """
    bot.delete_message(m.chat.id, m.message_id)
    try:
        count = bot.export_chat_invite_link(chat_id)
        bot.send_message(m.from_user.id, count)
    except:
        bot.send_message(
            chat_id,
            "К нам постучался заблокированный юзер " + m.from_user.last_name)


@in_chat()
@bot.message_handler(commands=['invite'])  # Команда /ivnite
def invite(m):
    """Команда /invite отправляем пользователя за ссылкой приглашения в чат """
    bot.delete_message(m.chat.id, m.message_id)
    try:
        sent = bot.send_message(
            m.chat.id,
            "Чтобы получить ссылку на приглашение в чат, свяжитесь с "
            "администрацией \n@evil_cat_it \n@hh8oShjvjj89og995gui\n@"
            "frutitutitut\n@I_LOVE_ARCH")
        sleep(10)
        bot.delete_message(m.chat.id, sent.message_id)
    except Exception:
        Error(m, bot).error()


@in_chat()
@check_reply()
def delete(m):
    """ Удалить пересланное сообщение, не знаю зачем, но мне в кайф """
    bot.delete_message(m.chat.id, m.message_id)
    try:
        bot.delete_message(m.chat.id, m.reply_to_message.message_id)
    except Exception:
        Error(m, bot).error()
    except apihelper.ApiTelegramException:
        pass


@in_chat()
def post(m):
    """ Запостить текст на канал """
    bot.delete_message(m.chat.id, m.message_id)
    try:
        bot.send_message(group_id, m.text[6:])
        bot.send_message(
            m.chat.id,
            "Сообщение \n {0} \nОтправлено на канал {1}".format(m.text[6:],
                                                                group_id))
    except Exception:
        Error(m, bot).error()
