import telebot
import os

TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🔥 Welcome to CareerOS AI Bot!\nYour AI Mentor is Active.")

@bot.message_handler(commands=['test'])
def test(message):
    bot.reply_to(message, "📘 Test feature coming soon!")

bot.infinity_polling()
