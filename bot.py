import logging, telegram, signal, sys
from telegram.ext import CommandHandler
from telegram.ext import Updater

bot = telegram.Bot(token='282471240:AAGPCyfKcOsj9C9bqsSVsRXfb_0yuQ-LAJw')

def_chat_id = {'message': {'migrate_to_chat_id': 0, 'delete_chat_photo': False, 'new_chat_photo': [], 'entities': [{'length': 6, 'type': u'bot_command', 'offset': 0}], 'text': u'/start', 'migrate_from_chat_id': 0, 'channel_chat_created': False, 'from': {'username': u'azide0x37', 'first_name': u'Alexander', 'last_name': u'Templeton', 'type': '', 'id': 138790512}, 'supergroup_chat_created': False, 'chat': {'username': '', 'first_name': '', 'all_members_are_admins': False, 'title': u"I'm gonna go take a shit", 'last_name': '', 'type': u'supergroup', 'id': -1001101556777L}, 'photo': [], 'date': 1494294819, 'group_chat_created': False, 'caption': '', 'message_id': 6530, 'new_chat_title': ''}, 'update_id': 113487707}

def signal_handler(signal, frame):
    print "Exiting program..."
    bot.send_message(chat_id=-1001101556777, text="SovPsy 7dtd bot shutting down...")
    sys.exit(0)
# TODO: Add proper logging of requests and errors in the future
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Define our command handling functions
def start(bot, update):
    print update.message.chat_id
    bot.send_message(chat_id=update.message.chat_id, text="This...is suprisingly easy as fuck.")

def clayton(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Clayton is retarded.")

def james(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Clayton is still retarded.")

if __name__ == '__main__':

    # Initialize a bot
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

    #Register with signal to send a shutdown message on exit/crash
    signal.signal(signal.SIGINT, signal_handler)

    # Show our bot server statistics 
    print(bot.get_me())

    # Log that bot is running
    bot.send_message(chat_id=-1001101556777, text="SovPsy 7dtd bot running...")
    updater.start_polling()
