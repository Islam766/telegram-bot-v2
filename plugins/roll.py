#!/usr/bin/python

import telebot
from telebot import types
import time
import random
from telebot import apihelper
from config import bot
from plugins.error import in_chat

text_info_user = {"names": [],
                  "colors": []
                }       #  для сохранения текста

def edit_message_callback(call):
    text_info = []

    keyboard = types.InlineKeyboardMarkup()
    keyboard_black = types.InlineKeyboardButton(text = "⚫ Чёрное ⚫", callback_data = f"black_roll")
    keyboard_red = types.InlineKeyboardButton(text = "🔴 Красное 🔴", callback_data = f"red_roll")
    keyboard_green = types.InlineKeyboardButton(text = "🟢 Зеленое 🟢", callback_data = f"green_roll")
    keyboard_roll = types.InlineKeyboardButton(text="Крутить", callback_data = "roll_fast")
    keyboard.add(keyboard_black, keyboard_red, keyboard_green)
    keyboard.add(keyboard_roll)

    ######### Нумерация каждого человека
    for name, color in zip(text_info_user["names"], text_info_user["colors"]):
        text_info.append(f" *{name}* - {color}")
    #########
    bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, 
                        text = "_На что желаете поставить ставки? Все ставки закроются через_ *10 секунд*\n\n" + "\n".join(text_info),
                        parse_mode = "Markdown", reply_markup = keyboard)

#########
def roll_function(): # Функция для определения победителя и расчета число
    number = random.randint(1, 100)
    winners_enum = []
    winners = []
    try:
                       # Если выиграли:
        if number == 1: # Зеленые
            for key, value in zip(text_info_user["names"], text_info_user["colors"]):
                if value == "🟢":
                    winners.append(key)
                    win_color = "зеро"

        if (number % 2) == 0: # Черные ⚫
            for key, value in zip(text_info_user["names"], text_info_user["colors"]):
                if value == "⚫":
                    winners.append(key)
                    win_color = "черное"

        if (number % 2) == 1: # Красные
            for key, value in zip(text_info_user["names"], text_info_user["colors"]):
                if value == "🔴":
                    winners.append(key)
                    win_color = "красное"

        for ind, val in enumerate(winners, 1):
            winners_enum.append(f"_{ind}._ *{val}*")

        winners_enum = "\n".join(winners_enum)
        
        return (winners_enum, win_color)
    except:
        return None
#########

@in_chat()
def roll(m):
    global text_info_user
    try:
        del roll.__annotations__["fast_roll"]
    except KeyError: pass

    text_info_user = {"names": [],
                  "colors": []
                }       #  для сохранения текста

    try:
        ######### Кнопки для удаления сообщения
        keyboard_delete_last = types.InlineKeyboardMarkup()
        keyboard_delete = types.InlineKeyboardButton(text = "❌", callback_data = "delete")
        keyboard_delete_last.add(keyboard_delete)
        #########

        ######### Удаление сообщения
        bot.delete_message(m.chat.id, m.message_id)
        #########

        ######### Кнопки, '&&' используется для разделителя, через callback'и отправляем по ним id следующего сообщения
        keyboard = types.InlineKeyboardMarkup()
        keyboard_black = types.InlineKeyboardButton(text = "⚫ Чёрное ⚫", callback_data = f"black_roll")
        keyboard_red = types.InlineKeyboardButton(text = "🔴 Красное 🔴", callback_data = f"red_roll")
        keyboard_green = types.InlineKeyboardButton(text = "🟢 Зеленое 🟢", callback_data = f"green_roll")
        keyboard.add(keyboard_black, keyboard_red)
        keyboard.add(keyboard_green)
        #########
        bot.send_message(m.chat.id, "_На что желаете поставить ставки? Все ставки закроются через_ *10 секунд*",
                        parse_mode = "Markdown", reply_markup = keyboard)

        time.sleep(10.0)
        try:
            roll.__annotations__["fast_roll"]
            del roll.__annotations__["fast_roll"]
        except KeyError:
            roll_winner = roll_function()

            if roll_winner is None:
                bot.edit_message_text(chat_id = m.chat.id, message_id = m.message_id + 1,
                                    text = f"_Увы, никто не выиграл!_",
                                    parse_mode = "Markdown")

            else:
                winners_enum, win_color = roll_winner
                bot.edit_message_text(chat_id = m.chat.id, message_id = m.message_id + 1,
                                    text = f" _Выпало_ *{win_color}* _Победители:_ \n\n {winners_enum}",
                                    parse_mode = "Markdown")
                time.sleep(5.0)
                bot.delete_message(m.chat.id, m.message_id)
    except (Exception, apihelper.ApiTelegramException) as e:
        pass
