

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
