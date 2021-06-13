#!/usr/bin/python
# -*- coding: utf8 -*-

from typing import Union
import random
from time import sleep

import telebot
import requests

from config import bot
from config import chat_id
from config import token

Exception_ = telebot.apihelper.ApiTelegramException

class Error:
    """ Обработчик ошибок """
    def __init__(self, m, bot):

        permission = ['У вас нет прав на использование этой команды',
                      'Недостаточно прав',
                      'Ну куда ты лезишь, команда не для тебя',
                      'Не делай так больше',
                      'Вот ты псих :D',
                      "А ну брысь отсюда",
                      "Ну и что ты хочешь от меня?",
                      "Ты действительно думаешь что я выполню твою просьбу?",
                      "Кышь, твои полномочия всё",
                      "Нет, я этого не сделаю"]

        reply = ['Перешлите сообщение',
                 'По-моему где-то сообщение потерялось и до меня не дошло',
                 'А сообщение где?',
                 'Я бы пошутил про UDP, но боюсь, что не дайдет, как и ваше п'
                 'ересланное сообщение', 
                 "А пересылать сообщение кто будет?"]

        admin = ['Я не имею прав трогать админов',
                 'Мои чары на администрацию не распространяется',
                 'А может не будем трогать админов?',
                 'Не надо раздражать админов',
                 'Ну это пиздец,' 
                 'зачем мы админов тронули, ну все, пойду вешаться',
                 "На что ты меня подписываешь? Не трошь админов",
                 "Не надо расстраивать администрацию"]

        errors = ['Ошибка', 
                  'Ой, я ошибку поймал',
                  "Я поймал KERNEL PANIC",
                  "Что-то мне сегодня не хорошо",
                  "Произошла ошибка, но я все равно буду работать"]

        private = ['Команда не работает в лс бота',
                   'Команда работает только в чате', 
                   'Ну и зачем ты это делаешь? Эта команда не для лс']

        shout = ['Крик из толпы',
                 'Я слышал, как кто-то крикнул',
                 "Какеры пришли и написали"]

        self.permission = permission
        self.reply = reply
        self.admin = admin
        self.errors = errors
        self.private = private
        self.shout = shout
        self.m = m
        self.bot = bot

    def error_reply_message(self):
        """ Функция для вывода ошибки, если нет пересланного сообщения """
        text = "❗⛔️ " + random.choice(self.reply) + " ⛔️❗"
        self.bot.send_message(self.m.chat.id, text)
        sleep(5)

        self.bot.delete_message(self.m.chat.id, self.m.message_id + 1)

    def error_permission(self):
        """ Функция для вывода ошибки, если ошибка при выполнение команды """
        text = "❗⛔️ " + random.choice(self.permission) + " ⛔️❗️"
        self.bot.send_message(self.m.chat.id, text)
        sleep(10)

        self.bot.delete_message(self.m.chat.id, self.m.message_id + 1)

    def message_admin(self):
        """ Функция для вывода ошибки, если сообщение принадлежит админу """
        text = "❗⛔️ " + random.choice(self.admin) + " ⛔️❗️"
        self.bot.send_message(self.m.chat.id, text)
        sleep(10)

        self.bot.delete_message(self.m.chat.id, self.m.message_id + 1)

    def error(self):
        """ В случае ошибки """
        text = "❗⛔️ " + random.choice(self.errors) + " ⛔️❗️"
        self.bot.send_message(self.m.chat.id, text)
        sleep(10)

        self.bot.delete_message(self.m.chat.id, self.m.message_id + 1)

    def private_bot(self):
        """ 
        Функция для вывода ошибки,
        если команда не предназначена для лс бота
        """

        text = "❗⛔️ " + random.choice(self.private) + " ⛔️❗️"
        self.bot.send_message(self.m.chat.id, text)
        sleep(5)

        self.bot.delete_message(self.m.chat.id, self.m.message_id + 1)

    def check_reply_admin_(self) -> Union[bool, None]:
        """ Проверка пересылается ли сообщение админу 

            True -  не администратор
            False - администратор
            None - сообщение не пересылалось
        """
        if self.m.reply_to_message:
            if self.bot.get_chat_member(chat_id,
                                        self.m.reply_to_message.from_user.id
                                        ).status not in ['administrator',
                                                         'creator']:
                return True
            return False
        return None


def in_chat():
    """ Проверка, присутствует ли человек в чате """
    def wrap1(func):
        def wrap2(message, *args):
            status = ['creator', 'administrator', 'member', "restricted"]
            if bot.get_chat_member(chat_id,
                                   user_id=message.from_user.id
                                   ).status in status:
                func(message, *args)
            else:
                bot.delete_message(message.chat.id, message.message_id)
                Error(message, bot).error()
        return wrap2
    return wrap1


def check_admin():
    """ Проверка, является ли человек администратором """
    def wrap1(func):
        def wrap2(message, *args):
            if bot.get_chat_member(chat_id,
                                   message.from_user.id
                                   ).status in ['administrator', 'creator']:
                func(message, *args)
            else:
                bot.delete_message(message.chat.id, message.message_id)
                Error(message, bot).error_permission()
        return wrap2
    return wrap1


def check_reply_admin():
    """ Проверка, чьё сообщение переслали """
    def wrap1(func):
        def wrap2(message, *args):
            if message.reply_to_message:
                if bot.get_chat_member(chat_id,
                                       message.reply_to_message.from_user.id
                                       ).status not in ['administrator',
                                                        'creator']:
                    func(message, *args)
                else:
                    bot.delete_message(message.chat.id, message.message_id)
                    Error(message, bot).message_admin()

        return wrap2
    return wrap1


def check_reply():
    """ Проверка, чьё сообщение переслали """
    def wrap1(func):
        def wrap2(message, *args):
            if message.reply_to_message:
                func(message, *args)
            else:
                bot.delete_message(message.chat.id, message.message_id)
                Error(message, bot).error_reply_message()
        return wrap2
    return wrap1


def check_private():
    """ Проверка, активен ли бот в личке """
    def wrap1(func):
        def wrap2(message, *args):
            if message.chat.type != "private":
                func(message, *args)
            else:
                bot.delete_message(message.chat.id, message.message_id)
                Error(message, bot).private_bot()
        return wrap2
    return wrap1


def check_exist_user():
    """ Проверка, существует ли пользователь (пересылающий) """
    def wrap1(func):
        def wrap2(message, *args):
            if message.reply_to_message:
                id_ = message.reply_to_message.from_user.id

                url = f'https://api.telegram.org/bot{token}/getChatMember'
                payload = {

                    "chat_id": "-1001293845658",
                    "user_id": id_
                }

                res = requests.post(url, data=payload)
                response = dict(res.json())
                response = response['result']
                status = response['status']
                try:
                    if status == 'left' or response['is_member'] is False:
                        bot.delete_message(message.chat.id, message.message_id)
                        Error(message, bot).error()
                    else:
                        func(message, *args)
                except Exception:
                    func(message, *args)
        return wrap2
    return wrap1
