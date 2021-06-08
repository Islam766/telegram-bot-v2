#!/usr/bin/python

from config import chat_id
from config import token
import requests
import json
from collections import namedtuple

############################################################################################
# Получение прав юзера
def getChatMember(id_, token = token):

    url = f'https://api.telegram.org/bot{token}/getChatMember'
    payload = {
        
        "chat_id": str(chat_id),
        "user_id": str(id_)
    }

    res = requests.post(url, data=payload)
    response = dict(res.json())
    response = response['result']
    if response['status'] == 'member':
        can_send_messages = True
        can_send_media_messages = True
        can_send_polls = True
        can_send_other_messages = True
        can_change_info = False
        can_invite_users = False
        can_pin_messages = False

    if response['status'] == 'restricted':
        for line in ['can_send_messages', 'can_send_media_messages','can_send_polls', 'can_send_other_messages', "can_change_info", 'can_invite_users', 'can_pin_messages']:
            if response[line]:
                bool_ = True
                if line == 'can_send_messages':
                    can_send_messages = bool_
                if line == 'can_send_media_messages':
                    can_send_media_messages = bool_
                if line == 'can_send_polls':
                    can_send_polls = bool_
                if line == 'can_send_other_messages':
                    can_send_other_messages = bool_
                if line == "can_invite_users":
                    can_invite_users = bool_
                if line == "can_pin_messages":
                    can_pin_messages = bool_
                if line == "can_change_info":
                    can_change_info = bool_
            else:
                bool_ = False
                if line == 'can_send_messages':
                    can_send_messages = bool_
                if line == 'can_send_media_messages':
                    can_send_media_messages = bool_
                if line == 'can_send_polls':
                    can_send_polls = bool_
                if line == 'can_send_other_messages':
                    can_send_other_messages = bool_
                if line == "can_invite_users":
                    can_invite_users = bool_
                if line == "can_pin_messages":
                    can_pin_messages = bool_
                if line == "can_change_info":
                    can_change_info = bool_
    rules = namedtuple("Permission", "can_send_messages can_send_media_messages can_send_polls can_send_other_messages can_invite_users can_pin_messages can_change_info")
    user_rules = rules(can_send_messages, can_send_media_messages, can_send_polls, can_send_other_messages, can_invite_users = False, can_pin_messages = False, can_change_info = False)
    return user_rules
