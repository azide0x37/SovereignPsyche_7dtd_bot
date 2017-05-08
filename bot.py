import telegram
bot = telegram.Bot(token='TOKEN')

if __name__ == '__main__':
    print(bot.get_me())
