#!/usr/bin/python
# -*- coding: utf8 -*-

try:
    from config import bot
    from config import botReserve
    from plugins.callback import callback_inline
    from plugins.kick import kick
    from plugins.mute import mute, unmute
    from plugins.pin import pin, unpin
    from plugins.base import encode, decode
    from plugins.start import start, helps
    from plugins.service import handler_new_member, left_chat_member
    from plugins.say import say
    from plugins.banner import banner, on
    from plugins.chat import description, link, invite, delete, post, id_chat
    from plugins.wiki import wikipedia
    from plugins.screenshot import screen
    from plugins.cats import cats
    from plugins.github import github
    from plugins.command_id import command_id
    from plugins.translation import en, ru
    from plugins.game import game
    from plugins.search import search, search_youtube
    from plugins.proxy import proxy
    from plugins.top import top, deletedb, createdb, write
    from plugins.news import news
    from telebot import types
    from plugins.error import Error
    from telebot.apihelper import ApiTelegramException
    from plugins.whois import whois
    from plugins.kernel import kernel
    from plugins.unban import unban
    from plugins.getchatmember import getChatMember
    from plugins.arch_news import arch__news
    from plugins.roll import roll
    from plugins.ping_pong import ping
    from plugins.ping_pong import date_start
    from plugins.crocodile import crocodile
    from plugins.crocodile import crocodile_win
    from plugins.get_up_bitch import get_up

    from manage import restart_
    from manage import autorestart__


    date_start()  # Время, при котором был запущен бот

    bot.remove_webhook()  # отключает вебхук
    banner()  # выводим баннер

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @botReserve.message_handler(commands=["restart"])
    def restart(message):
        """ Принудительная перезагрузка бота """
        restart_(message)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @bot.message_handler(commands=["get_up"])
    def get_up_(message):
        """ Поднимает пользователя """
        get_up(message)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @bot.message_handler(commands=["crocodile"])
    def crocodile_play(message):
        """ Игра крокодил для хардкорщиков """
        crocodile(message)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @bot.message_handler(commands=["roll"])
    def roll_play(message):
        """ Игра рулетка """
        roll(message)
   
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @bot.message_handler(commands=["ping"])
    def ping_test(message):
        """ Ping бота """
        ping(message)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @bot.message_handler(commands=['news'])
    def new(message):
        """ Показывает новости OpenNet'а """
        news(message)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @bot.message_handler(commands=['deletedb'])
    def delete_database(message):
        """ Удаляет базу """
        deletedb(message)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @bot.message_handler(commands=['createdb'])
    def create_database(message):
        """ Создает базу """
        createdb(message)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @bot.message_handler(commands=['top'])
    def top_users(message):
        """ Показывает активность пользователей """
        top(message)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @bot.message_handler(commands=['proxy'])
    def proxys(message):
        """ Список с проксями """
        proxy(message)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @bot.message_handler(commands=['sy'])
    def searchs_youtube(message):
        """ Поиск в ютубе """
        search_youtube(message)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @bot.message_handler(commands=['search'])
    def searchs(message):
        """ Поиск в утке """
        search(message)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @bot.message_handler(commands=['chat_id'])
    def id_chats(message):
        """ Вывод айди чата """
        id_chat(message)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @bot.message_handler(commands=['game'])
    def games(message):
        """ Игра 'камень-ножницы-бумага' """
        game(message)
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    @bot.message_handler(content_types=['pinned_message'])
    def pindel(message):
        """ Прикрепляет сообщение """
        bot.delete_message(message.chat.id, message.message_id)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @bot.message_handler(commands=['encode'])
    def encodes(message):
        """ Декодирование в BASE64 """
        encode(message)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @bot.message_handler(commands=['decode'])
    def decodes(message):
        """ Перевод из BASE64 """
        decode(message)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @bot.message_handler(commands=["mute"])
    def test(message):
        """ Замутить пользователя """
        mute(message)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @bot.message_handler(commands=["unmute"])
    def unmuting(message):
        """ Размутить пользователя """
        unmute(message)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @bot.message_handler(commands=["pin"])
    def pins(message):
        """ Прикрепить сообщение """
        pin(message)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @bot.message_handler(commands=["unpin"])
    def unpins_(message):
        """ Открепление сообщения """
        unpin(message)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @bot.message_handler(commands=['say'])
    def says(message):
        """ Анонимное сообщение """
        say(message)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @bot.message_handler(content_types=['left_chat_member'])
    def left_chat_members(message):
        """ Прощаемся с вышедшим с чата """
        left_chat_member(message)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @bot.message_handler(content_types=["new_chat_members"])
    def handler_new_members(message):
        """ Приветствуем нового пользователя """
        handler_new_member(message)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @bot.message_handler(commands=["kick"])
    def kickid(message):
        """ Команда кика """
        kick(message)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @bot.message_handler(commands=['start'])
    def any_start(message):
        """ Менюшка для пользователя """
        start(message)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @bot.message_handler(commands=['help'])
    def any_help(message):
        """ Список с доступными командами """
        helps(message)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @bot.callback_query_handler(func=lambda call: True)
    def callback_inlines(call):
        """ Кнопки """
        callback_inline(call)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @bot.message_handler(commands=['ru'])
    def russian(message):
        """ Перевод на англ """
        ru(message)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @bot.message_handler(commands=['en'])
    def english(message):
        """ Перевод на русский """
        en(message)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @bot.message_handler(commands=['id'])
    def commands_id(message):
        """ Опредение ID пользователя """
        command_id(message)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @bot.message_handler(commands=["logs"])
    def logs(message):
        """ Логгирование """
        bot.delete_message(message.chat.id, message.message_id)
        if bot.get_chat_member(message.chat.id, message.from_user.id).status in ["administrator", "creator"]:
            keyboard = types.InlineKeyboardMarkup()
            keyboard_delete = types.InlineKeyboardButton(text="❌", callback_data="delete")
            keyboard.add(keyboard_delete)
            FILE = open("plugins/log-error.txt", "rb")
            bot.send_document(message.chat.id, FILE, reply_markup=keyboard, parse_mode="Markdown")
            FILE.close()
        else:
            Error(m,bot).error_permission()

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @bot.message_handler(regexp=r'^[^./].*(инд)[ауя]')
    def windows(message):
        bot.send_sticker(
                message.chat.id,
                "CAACAgQAAxkBAALoU17aTycp4L0kAkIssMm9au-ZFzIAAxQAA7p6vBnUv7ww6"
                "GyZrhoE")

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @bot.message_handler(commands=['post'])
    def posts(message):
        """ Команда для публикации анекдота """
        post(message)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @bot.message_handler(commands=['del'])
    def deletes(message):
        """ Удаление сообщения """
        delete(message)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @bot.message_handler(commands=['github'])
    def git(message):
        """ Вывод гитхаба """
        github(message)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @bot.message_handler(commands=['invite'])
    def invites(message):
        """ Выводим как пригласить людей """
        invite(message)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @bot.message_handler(commands=['cats'])
    def cat(message):
        """ Получение котят """
        cats(message)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @bot.message_handler(commands=['url'])
    def url(message):
        """ Получение скриншота ссылки """
        screen(message)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @bot.message_handler(commands=['link'])
    def links(message):
        """ Получение ссылки приглашение """
        link(message)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @bot.message_handler(commands=['wiki'])
    def wiki(message):
        """ Поиск в Википедии """
        wikipedia(message)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @bot.message_handler(commands=['des'])
    def chat(message):
        """ Изменение описания чата """
        description(message)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @bot.message_handler(commands=["whois"])
    def who(message):
        """ Получение информации об IP """
        whois(message)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @bot.message_handler(commands=["kernel"])
    def kernel_parsing(message):
        """ Получение версий ядер """
        kernel(message)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @bot.message_handler(commands=["unban"])
    def unban_member(message):
        """ Разблокировка пользователя """
        unban(message)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @bot.message_handler(commands=["arch_news"])
    def arch_news_parsing(message):
        """ Получение новостей арча """
        arch__news(message)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    @botReserve.message_handler(func=lambda message: True,
                                content_types=["text",
                                               "sticker",
                                               "photo",
                                               "audio",
                                               "video",
                                               "document"])
    def autorestart(m):
        autorestart__(m)


    @bot.message_handler(func=lambda message: True, content_types=["text",
                                                                   "sticker",
                                                                   "photo",
                                                                   "audio",
                                                                   "video",
                                                                   "document"])
    def writes_users(message):
        try:
            write(message)
            if message.text.lower() in crocodile.__annotations__["word_txt"]:
                crocodile_win(message)
        except (ApiTelegramException):
            pass
    on()
    try:
        bot.polling()
        botReserve.polling()
    except RecursionError:
        pass
except (RecursionError) as e:
    print("❌_____________________________________❌")
    print("❌❌❌ОШИБКА❌❌❌")
    print(e)
    print("❌_____________________________________❌")
