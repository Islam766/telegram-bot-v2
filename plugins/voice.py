from config import bot
from config import s
import speech_recognition as sr #pip install SpeechRecognition
import subprocess
import os
import urllib.request #pip install urllib3
import json
from config import token
from plugins.error import in_chat

@in_chat()
def voice(message):
    request2text(message.voice.file_id, message.chat.id)

def wav2text(dest_filename, id, file_name):
    r = sr.Recognizer()
    message = sr.AudioFile(dest_filename)
    with message as source:
        audio = r.record(source)
    try:
        result = r.recognize_google(audio, language="ru_RU")
        bot.send_message(id, format(result))
        os.remove(dest_filename)
        os.remove(file_name)
    except sr.UnknownValueError:
        bot.send_message(id, 'Говори четче')
        os.remove(dest_filename)
        os.remove(file_name)

def oga2wav(file_name, id):
    try:
        src_filename = file_name
        dest_filename = file_name + '.wav'
        process = subprocess.run(['ffmpeg', '-i', src_filename, dest_filename]) #Специально написана переменная, которая не используется, чтобы голосовые не сохраняла на хостинге
        wav2text(dest_filename, id, file_name)
    except (Exception, sr.UnknownValueError) as e:
        print ("voice.py | oga2wav: ", e, sep = "")  

def donwload(file_path, file_id, id):
    try:
        url = f'https://api.telegram.org/file/bot{token}/' + file_path
        urllib.request.urlretrieve(url, file_id + '.oga')
        file_name = file_id + '.oga'
        oga2wav(file_name, id)
    except (Exception, sr.UnknownValueError) as e:
        print ("voice.py | donwload: ", e, sep = "")

def request2text(file_id, id):
    try:
        r = s.get(f'https://api.telegram.org/bot{token}/getFile?file_id=' + file_id)
        r = json.loads(r.text)
        donwload(r['result']['file_path'], r['result']['file_id'], id)
    except (Exception, sr.UnknownValueError) as e:
        print ("voice.py | request2text: ", e, sep = "")