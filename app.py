import telegram.ext
import os
from dotenv import load_dotenv
import requests


load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')


def start(update, context):
    update.message.reply_text("hello! Let's drink water!")

def get_stock_price(stockName):

    r = requests.get("https://kams-stocks.herokuapp.com/infosys").json()
    return(r['stockPrice'])


def help(update, context):
    update.message.reply_text("""
    You can use the following commands:
    /start -> greeting
    /contact -> contact details
    /content -> some content
    """)


def stock(update, context):
    ticker = context.args[0]
    price = get_stock_price(ticker)
    update.message.reply_text(
        "Current price of {0} is {1}".format(ticker, price,))


def content(update, context):
    update.message.reply_text("Let's laugh at  fools hahahahahaha")


def contact(update, context):
    update.message.reply_text(
        "contacct me through email - kamathapp7@gmail.com")


def handle_message(update, context):
    update.message.reply_text("You entered {0}".format(update.message.text,))


updater = telegram.ext.Updater(TELEGRAM_TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("contact", contact))
disp.add_handler(telegram.ext.CommandHandler("content", content))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("stock", stock))
disp.add_handler(telegram.ext.MessageHandler(
    telegram.ext.Filters.text, handle_message))

updater.start_polling()
updater.idle()
