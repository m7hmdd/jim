import requests, user_agent, json, flask, telebot, random, os, sys, time
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from flask import Flask, request

BOT_TOKEN = "1198344060:AAEZsNjFn9TGf82a6XX2gow7VXbCe3lFloY"
bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)

@bot.message_handler(content_types=['text'])
def Send(message):
        user =[]
        count = 0
        if "-" in message.text and message.text.split("-")[0] != '' and message.text.split("-")[1] != '':
            username = message.text.split("-")[1]
            user.append(username)
            token = message.text.split("-")[0]
            url = "https://botapi.tamtam.chat/"
            params = {"access_token": token}
            method = 'me'
            data = {
                "username": username
            }
            
            infoM = bot.send_message(message.chat.id, "[+]Username :: {}".format(username))
            for i in range(10000):
                response = requests.patch(url + method, params=params, data=json.dumps(data)).text
                # if '"This name is already in use"' in response :

                if '"username":"{}"'.format(username) in response:
                    bot.send_message(message.chat.id, "[+]Done Hunted\n— — — —\n[+]Username :: {}\n[+]Requests Number :: {}".format(username, count))
                    a = requests.patch(url + method, params=params, data=json.dumps(data)).text
                    print(a)
                    break
                elif 'Invalid access_token:' in response:
                    bot.send_message(message.chat.id, 'Send Right Token')
                    break
                else:
                    count += 1
                    bot.edit_message_text(chat_id=message.chat.id, message_id=infoM.message_id, text="[+]Username :: {}\n[+]Requests Number :: {}".format(username, count))

        elif "/chec" in message.text:
            bot.send_message(message.chat.id,  "[+]Username :: {}\n[+]Requests Number :: {}".format(user[0], count))
        else:
            bot.send_message(message.chat.id, "[+]Send Information Like :\nToken-username")


            
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
