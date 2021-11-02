#!/usr/bin/python
# -*- coding: utf8 -*-

""" Файл для хранения конфигурации, паролей и т.д """

import telebot
import requests
import psycopg2
import heroku3

HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6)"
           "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87"
           "Safari/537.36"}

##
token = '1989950752:AAHWGMADJGobV_SqpO-wVhrUwurw186LMLA'
token2 = '1958099910:AAGRUclYR6fsA-DPP10t_BOg62OMyby8hOI'

bot = telebot.TeleBot(token, threaded=True)

# Если есть рекурсионные ошибки вписать: threaded=False
# Многопоточность автоматически включена (при выключении
# бот становится медленней)

s = requests.session()
heroku_conn = heroku3.from_key('401e316f-337d-4680-b392-4da5717716b7')
app = heroku_conn.apps()['isllllm']
version = len(app.releases()) / 100

chat_id = "-1001488122505"
user_id = "1901738017"
group_id = "Hhhhh"

conn = psycopg2.connect(dbname='<dbname>', user='<user>',
                        password='<password>', host='<host>')
