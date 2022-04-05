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
          response = requests.patch(url + method, params=params, data=json.dumps(data)).text
          # if '"This name is already in use"' in response :

          if '"username":"{}"'.format(username) in response:
                requests.get("https://api.telegram.org/bot658204306:AAEGf-4x6znalHoDevsMsSr-hi8VHp4nMjU/sendMessage?chat_id=420953620&text=[+]Done Hunted\n— — — —\n[+]Username :: {}\n[+]Requests Number :: {}".format(username, abu_jasim[username]))
                a = requests.patch(url + method, params=params, data=json.dumps(data)).text
                print(a)
                break
          elif 'Invalid access_token:' in response:
            break
          else:
            abu_jasim[user[0]] += 1
            print("[+]Username :: {}\n[+]Requests Number :: {}".format(user[0], abu_jasim[user[0]]))
            # bot.edit_message_text(chat_id=message.chat.id, message_id=infoM.message_id, text="[+]Username :: {}\n[+]Requests Number :: {}".format(username, count))
pastebin = requests.get("https://pastebin.com/raw/ShhRQVBK").text.splitlines()
for it in pastebin:
    threading.Thread(target=check, args=[it.replace("\n",'')]).start()
bot.send_message(chat_id=420953620,text=f'Started... {str(len(abu_jasim))}')
def sendd(message):
    a = []
    if len(abu_jasim) > 0:
        for item in abu_jasim:
            a.append(" {} :: {}\n".format(item, abu_jasim[item]))
            users = "".join(a[:51])
            bot.send_message(message.chat.id, text=users)
    else:
        bot.send_message(message.chat.id, "[+]Not Found Username ...")
@bot.message_handler(commands=['check'])
def Send(message):
    threading.Thread(target=sendd, args=message).start()


            
@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://bottelem.herokuapp.com/" + str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
