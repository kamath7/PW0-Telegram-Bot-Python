import telegram.ext
import os
from dotenv import load_dotenv

load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

def start(update, context):
    update.message.reply_text("hello! Let's drink water!")

def help(update, context):
    update.message.reply_text("""
    You can use the following commands:
    /start -> greeting
    /contact -> contact details
    /content -> some content
    """)

def content(update, context):
    update.message.reply_text("Let's laugh at  fools hahahahahaha")

def contact(update, context):
    update.message.reply_text("contacct me through email - kamathapp7@gmail.com")

updater = telegram.ext.Updater(TELEGRAM_TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("contact", contact))
disp.add_handler(telegram.ext.CommandHandler("content", content))
disp.add_handler(telegram.ext.CommandHandler("help", help))

updater.start_polling()
updater.idle()