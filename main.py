import requests, user_agent, json, flask, telebot, random, os, sys, time, threading
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from flask import Flask, request

BOT_TOKEN = "5295940154:AAGZc95-F6VltntXMGDGIsyRb21qI8EIZwQ"
bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)

@bot.message_handler(commands=['start'])
def start(message):
    key = types.InlineKeyboardMarkup()
    key.row_width = 2
    btn1 = types.InlineKeyboardButton(text=f"- تحميل فيديو .",callback_data="vid")
    btn2 = types.InlineKeyboardButton(text=f"- تحميل صوت .",callback_data="mp3")
    btn3 = types.InlineKeyboardButton(text=f"- المبرمق .",url="https://t.me/revengereback")
    key.add(btn1,btn2)
    key.add(btn3)
    bot.reply_to(message,f"- اهلا بك في بوت تحميل يوتيوب\n- يمكنك التحكم من الاسفل ادناه ..\n- @trprogram .",reply_markup=key)
@bot.callback_query_handler(func=lambda m:True)
def qu(call):
    if call.data == "vid":
        mm = bot.send_message(call.message.chat.id,f"- قم بأرسال كلمة للبحث عن الفيديو .")
        bot.register_next_step_handler(mm,downVid)
    if call.data == "mp3":
        mm = bot.send_message(call.message.chat.id,f"- قم بأرسال كلمة للبحث عن الفيديو .")
        bot.register_next_step_handler(mm,downMp3)
def downVid(message):
    lii = message.text
    p = bot.send_message(message.chat.id,f"- يتم البحث الان ..")
    ul = requests.get(f"https://mr-abood.herokuapp.com/YouTube/Videos/Search?query={lii}&page=1")
    if "id" in ul.text:
        id = ul.json()[0]['id']
        print(id)
        title = ul.json()[0]['title']
        dur = ul.json()[0]['duration']
        vi = ul.json()[0]['viewCount']['short']
        key2 = types.InlineKeyboardMarkup()
        key2.row_width = 1
        btn5 = types.InlineKeyboardButton(text=f"- المبرمق",url=f"https://t.me/RevengeReback")
        key2.add(btn5)
        rtr = requests.get('https://yoodownload.com/').text
        token = re.findall('<input name="token" type="hidden" value="(.*?)">',rtr)[0]
        
        hheaders = {
    # trakos headers
    'authority': 'yoodownload.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    'cookie': '_ga=GA1.2.89962626.1659127863; _gid=GA1.2.21866011.1659127863; _gat=1',
    'origin': 'https://yoodownload.com',
    'referer': 'https://yoodownload.com/index.php?error=41',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}
        dataa = {
    'u': f'https://youtu.be/{id}',
    'token': f'{token}',
        }

        response = requests.post('https://yoodownload.com/download.php', headers=hheaders, data=dataa).text
        lil = (re.findall('href="(.*?)"',response)[20])
        bot.delete_message(chat_id=message.chat.id,message_id=p.message_id)
        bot.send_video(message.chat.id,lil,caption=f"- العنوان : {title}\n- المشاهدات : {vi}",reply_markup=key2)
    else:
        bot.reply_to(message,f"صار خطأ ..")
def downMp3(message):
    lii = message.text
    p = bot.send_message(message.chat.id,f"- يتم البحث الان ..")
    ul = requests.get(f"https://mr-abood.herokuapp.com/YouTube/Videos/Search?query={lii}&page=1")
    if "id" in ul.text:
        id = ul.json()[0]['id']
        print(id)
        title = ul.json()[0]['title']
        dur = ul.json()[0]['duration']
        vi = ul.json()[0]['viewCount']['short']
        key2 = types.InlineKeyboardMarkup()
        key2.row_width = 1
        btn5 = types.InlineKeyboardButton(text=f"- المبرمق",url=f"https://t.me/RevengeReback")
        key2.add(btn5)
        rtr = requests.get('https://yoodownload.com/').text
        token = re.findall('<input name="token" type="hidden" value="(.*?)">',rtr)[0]
        
        headers = {
    'authority': 'api.onlinevideoconverter.pro',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    # Already added when you pass json=
    # 'content-type': 'application/json',
    'origin': 'https://en.onlinevideoconverter.pro',
    'referer': 'https://en.onlinevideoconverter.pro/',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}

        json_data = {
    'url': f'https://youtu.be/{id}',
    'converter': 'ffmpeg-mp3',
}

        response = requests.post('https://api.onlinevideoconverter.pro/api/convert', headers=headers, json=json_data).json()['resource']['taskName']
        bot.delete_message(chat_id=message.chat.id,message_id=p.message_id)
        bot.send_voice(message.chat.id,f"https://en.onlinevideoconverter.pro/api/storage/{response}",caption=f"- العنوان : {title}\n- المشاهدات : {vi}",title="FuckOff",reply_markup=key2)
    else:
        bot.reply_to(message,f"صار خطأ ..")


@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://temidolebot.herokuapp.com/" + str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
