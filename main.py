import os
import telebot
import google.generativeai as genai
from flask import Flask, request

# ඔබේ API Key එක Railway Variables වලින් ලබාගන්න
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

TOKEN = "8919957546:AAHAGXrPUJzJFo1CU35j81m2kxGo3z7j1Rw"
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        # AI එකෙන් පිළිතුරු ලබාගැනීම
        response = model.generate_content(message.text)
        
        if response.candidates and response.candidates[0].content.parts:
            text = response.candidates[0].content.parts[0].text
            bot.reply_to(message, text)
        else:
            bot.reply_to(message, "මට ඒකට උත්තරයක් දෙන්න බැරි වුණා.")
    except Exception as e:
        bot.reply_to(message, f"දෝෂයක් ඇතිවිය: {str(e)}")

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    # මෙතන 'ඔයාගේ_බොට්_ලින්ක්_එක' වෙනුවට ඔබේ Railway URL එක දාන්න
    bot.set_webhook(url='https://web-production-f7679.up.railway.app/' + TOKEN)
    return "!", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

