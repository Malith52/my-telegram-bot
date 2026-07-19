import os
import telebot
from flask import Flask, request

TOKEN = "8919957546:AAHAGXrPUJzJFo1CU35j81m2kxGo3z7j1Rw"
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # මෙතනට ඔයාගේ AI logic එක දාන්න පුළුවන්
    bot.reply_to(message, "ඔයාගේ බොට් සාර්ථකව වැඩ කරනවා!")

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='ඔයාගේ_බොට්_ලින්ක්_එක/' + TOKEN)
    return "!", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
