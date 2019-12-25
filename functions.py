from bot import *
import requests
CONST_URL = "https://api.telegram.org/bot708914610:AAFtLSerk5aw-72yKKvljZbrrRSmd4yHV8I/"
from time import sleep

#admin id 60201964
class functional:
    def __init__(self):
        self.bot = bot()
    def send_message(self, id, message):
        bot.send_message( id, message)
    send_message(60201964, 'ты админ?')

    def get_updates_json(self,request):
        params = {'timeout': 100, 'offset': None}
        response = requests.get(request + 'getUpdates', data=params)
        return response.json()

    def get_chat_id(self,update):
        chat_id = update['message']['chat']['id']
        return chat_id

    def last_update(self,data):
        results = data['result']
        total_updates = len(results) - 1
        return results[total_updates]

    def get_chat_text(self,update):
        chat_text = update['message']['text']
        return chat_text

    def send_mess(self,chat, text):
        params = {'chat_id': chat, 'text': text}
        response = requests.post(CONST_URL + 'sendMessage', data=params)
        return response
    def send_mess_all(self,id_list, text):
        for id in id_list:
            params = {'chat_id': id, 'text': text}
            response = requests.post(CONST_URL + 'sendMessage', data=params)