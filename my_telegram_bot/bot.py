import telebot
import os

# از محیط Render مقدار توکن رو می‌گیریم
TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, f"سلام {message.from_user.first_name} 🌸\nمن روی Render اجرا می‌شم!")

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.reply_to(message, "دستورهای من:\n/start - شروع\n/help - راهنما")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, f"گفتی: {message.text}")

if __name__ == "__main__":
    print("ربات در حال اجراست 🚀")
    bot.polling(non_stop=True)
