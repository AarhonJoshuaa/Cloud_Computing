import telebot
from telebot import types
from settings import config
bot = telebot.TeleBot(config.telegram_key)
bot.remove_webhook()

@bot.message_handler(commands=['start'])
def _start(message):
    msg = "Hello "+str(message.chat.username)+", I'm a 🦜. I repeat what you say"
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id,msg,reply_markup=markup)
    
@bot.message_handler(func=lambda message: True)
def _start1(message):
    msg = message.text
    bot.send_message(message.chat.id,"🦜 says: "+msg)
    
    
if config.ENV == "DEV":
    bot.infinity_polling(True)  

elif config.ENV == "PROD":
    import flask
    server = flask.Flask(__name__)

    @server.route('/'+config.telegram_key, methods=['POST'])
    def getMessage():
        bot.process_new_updates([telebot.types.Update.de_json(flask.request.stream.read().decode("utf-8"))])
        return "!", 200

    @server.route("/")
    def webhook():
        bot.remove_webhook()
        if config.ENV == "PROD":
            bot.set_webhook(url='https://beat-the-bot.herokuapp.com/'+config.telegram_key)
            return 'Chat with the Bot', 200

    if __name__ == "__main__":
        server.run(host=config.host, port=config.port)
