import logging, telegram
from telegram.ext import CommandHandler
from telegram.ext import Updater

bot = telegram.Bot(token='282471240:AAGPCyfKcOsj9C9bqsSVsRXfb_0yuQ-LAJw')

updater = Updater(token='282471240:AAGPCyfKcOsj9C9bqsSVsRXfb_0yuQ-LAJw')
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="This...is suprisingly easy as fuck.")

def clayton(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Clayton is retarded.")

def james(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Clayton is still retarded.")

if __name__ == '__main__':
    #print(bot.get_me())
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    #start_handler = CommandHandler('clayton', clayton)
    #start_handler = CommandHandler('james', james)

    dispatcher.add_handler(start_handler)
    updater.start_polling()