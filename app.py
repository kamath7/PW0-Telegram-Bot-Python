import telegram.ext
import os
from dotenv import load_dotenv

load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

updater = telegram.ext.Updater(TELEGRAM_TOKEN, use_context=True)
disp = updater.dispatcher