#!/usr/bin/python
#import time
import telebot
from config import bot
import psycopg2

def check_root(m):
	import psycopg2
	conn = psycopg2.connect(dbname='bbn2n7gitwwguwfdher0', user='ususbnvggq8v2fb9gvht', password='32DSJWANbSKGQEwV6WLz', host='bbn2n7gitwwguwfdher0-postgresql.services.clever-cloud.com')
	cursor = conn.cursor()
	cursor.execute(f"SELECT row_number() OVER(ORDER BY message::int DESC), root FROM top_users WHERE user_id = {m.from_user.id};")
	rows = (cursor.fetchall())[0][1]
	return rows

def root(m):
	password = "fuck_the_system_chat_linux2020"
	password_for_user = (m.text).split()[1]       # Получаем пароль который ввел пользователь\

	if password == password_for_user and m.chat.type == "private":
		conn = psycopg2.connect(dbname='bbn2n7gitwwguwfdher0', user='ususbnvggq8v2fb9gvht', password='32DSJWANbSKGQEwV6WLz', host='bbn2n7gitwwguwfdher0-postgresql.services.clever-cloud.com')
		cursor = conn.cursor()
		bot.delete_message(m.chat.id, m.message_id)
		bot.send_message(m.chat.id, "*Вы получили рут права бота!*", parse_mode = "Markdown")
		bot.send_message(m.chat.id, "*Теперь Вам доступен весь функционал бота, чтобы увидеть разрешенные команды введите* `/help_root`",
			parse_mode = "Markdown")
		cursor.execute(f"""UPDATE top_users SET root = TRUE WHERE user_id = {m.from_user.id};""")
		conn.commit()
def help_root(m):
	bot.delete_message(m.chat.id, m.message_id)
	bot.send_message("""`/set` *ID* *Количество сообщений* - _Изменяет значение message в базе_
		\n `""")

