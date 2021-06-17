#!/usr/bin/python
# -*- coding: utf8 -*-

""" Файл для отображения баннера """


from colorama import Fore, Style


def banner():
    banner = '''
 _______          _________ _          _______  _______ _________
(  ____ \|\     /|\__   __/( \        (  ____ \(  ___  )\__   __/
| (    \/| )   ( |   ) (   | (        | (    \/| (   ) |   ) (
| (__    | |   | |   | |   | |        | |      | (___) |   | |
|  __)   ( (   ) )   | |   | |        | |      |  ___  |   | |
| (       \ \_/ /    | |   | |        | |      | (   ) |   | |
| (____/\  \   /  ___) (___| (____/\  | (____/\| )   ( |   | |
(_______/   \_/   \_______/(_______/  (_______/|/     \|   )_(
'''
    print(Fore.RED + banner)
    print(Style.RESET_ALL)


def on():
    """ Уведомляем, что бот запущен """
    on_text = "Бот запущен и ожидает сообщения"
    "(CTRL + C Чтобы выключить бота)"

    print(Fore.RED + on_text)
    print(Style.RESET_ALL)


def off():
    """ Уведомляем, что бот выключен """
    off_text = "Бот выключен"
    print(Fore.RED + off_text)
    print(Style.RESET_ALL)
