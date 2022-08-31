import requests, user_agent, json, flask, telebot, random, os, sys, time
import telebot
import threading
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from flask import Flask, request

BOT_TOKEN = "1132931143:AAGwzukJusNzc5XjSvIMS92X8qLtGo9_Im4"
bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)

abu_jasim = {}
def check(text):
      user = []
      count = 0
      username = text.split(":")[1]
      user.append(username)
      abu_jasim.setdefault(user[0], 0)
      token = text.split(":")[0]
      url = "https://botapi.tamtam.chat/"
      params = {"access_token": token}
      method = 'me'
      data = {
          "username": username
      }
      if ":" in text and text.split(":")[0] != '' and text.split(":")[1] != '':
        while True:


#token = "" # файл, содержащий 
from tambotapi import TamBot
import tambotapi
import json, os
import logging
from flask import Flask, request, jsonify  # для webhook


# }

token = "U1v2LMDR7nJ9kSU0j0LV9Qd3peQTFaW4-7oCN4zRLxc"


bot = TamBot(token)
logger = tambotapi.logger
logger.setLevel(logging.DEBUG)
app = Flask(__name__)  # для webhook
while True:
        upd = bot.get_updates()  # получаем внутреннее представление сообщения (контента) отправленного боту (сформированного ботом)
        # этот способ не формирует событие (mark_seen) о прочтении ботом сообщения, нужно формировать его самостоятельно 
        if upd:  # основной код, для примера представлен эхо-бот
            chat_id = bot.get_chat_id(upd)
            text = bot.get_text(upd)
            if text == "/start":
              bot.send_message("Hello", chat_id)

@app.route('/', methods=['POST'])  # для webhook
def main():
    while True:
        upd = bot.get_updates()  # получаем внутреннее представление сообщения (контента) отправленного боту (сформированного ботом)
        # этот способ не формирует событие (mark_seen) о прочтении ботом сообщения, нужно формировать его самостоятельно 
        if upd:  # основной код, для примера представлен эхо-бот
            chat_id = bot.get_chat_id(upd)
            text = bot.get_text(upd)
            if text == "/start":
              bot.send_message("Hello", chat_id)
            logger.info('Сообщение получено и отправлено')
        return jsonify(upd)  # для webhook


if __name__ == '__main__':  # для webhook
    try:
        app.run(port=int(os.environ.get("PORT", 5000)), host="0.0.0.0") # порт нужно выбирать нестандартный для уменьшения количества атак
    except KeyboardInterrupt:
        exit()
