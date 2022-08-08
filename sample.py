import requests
from urllib.request import urlopen
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("BOT API TOKEN (FROM BOT FATHER)",use_context=True)

def start(update: Update, context: CallbackContext):
	update.message.reply_text("Hello there, Welcome to the Bot.Please write /help to see the commands available.")

def help(update: Update, context: CallbackContext):
	update.message.reply_text("""Available Commands :-
	/start - Check if bot is alive
	/help - To get the help box
	/check - Check bot stauts with Google""")

def check(update: Update, context: CallbackContext):
update.message.reply_text("If the status returned is 200, it means the bot is working for. Not network issue.")
  response = requests.get('https://www.google.com')
  update.message.reply_text(response.text)

def unknown(update: Update, context: CallbackContext):
	update.message.reply_text("Sorry '%s' is not a valid command" % update.message.text)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('check', check))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))

updater.start_polling()