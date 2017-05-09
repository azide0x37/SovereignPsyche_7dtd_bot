import logging, telegram
from telegram.ext import CommandHandler
from telegram.ext import Updater

# TODO: Add proper logging of requests and errors in the future
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Define our command handling functions
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="This...is suprisingly easy as fuck.")

def clayton(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Clayton is retarded.")

def james(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Clayton is still retarded.")

if __name__ == '__main__':

    bot = telegram.Bot(token='282471240:AAGPCyfKcOsj9C9bqsSVsRXfb_0yuQ-LAJw')
    updater = Updater(token='282471240:AAGPCyfKcOsj9C9bqsSVsRXfb_0yuQ-LAJw')

    # Override other instances of server running elsewhere
    bot.setWebhook()

    # Add command handlers
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    #start_handler = CommandHandler('clayton', clayton)
    #start_handler = CommandHandler('james', james)

    dispatcher.add_handler(start_handler)

    # Server has started, log and notify admin
    print("Server is running")

    # Show our bot server statistics 
    print(bot.get_me())

    updater.start_polling()

