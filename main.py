from telegram.ext import Updater
from scholar import ScholarQuerier, SearchScholarQuery
import logging

updater = Updater(token='667003648:AAEAl3Z7SCy8c1WM3ITF7TY6G8oO-eTteic')

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me")

def search(bot, update, args):
    search_command = ' '.join(args)

    bot.send_message(chat_id=update.message.chat_id, text="You searched for: " + search_command)

    querier = ScholarQuerier()
    query = SearchScholarQuery()
    query.set_words(args)
    querier.send_query(query)
    
    articles = querier.articles
    
    message = ""

    bot.send_message(chat_id=update.message.chat_id, text="Number of results: " + str(len(articles)))

    index = 0
    for article in articles:
        bot.send_message(chat_id=update.message.chat_id, text=str(index+1)+". " + article.attrs['title'][0])


from telegram.ext import CommandHandler

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
search_handler = CommandHandler('search', search, pass_args=True)
dispatcher.add_handler(search_handler)

updater.start_polling()
