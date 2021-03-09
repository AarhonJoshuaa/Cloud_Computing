import telebot
from telebot import types
from settings import config
bot = telebot.TeleBot(config.telegram_key)
bot.remove_webhook()

@bot.message_handler(commands=['start'])
def _start(message):
    msg = "Hello "+str(message.chat.username)+", I'm a 🦜. I repeat what you say"
    print(msg)
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id,msg,reply_markup=markup)
    
@bot.message_handler(func=lambda message: True)
def _start1(message):
    msg = message.text
    if(msg=='apoorva'):
        bot.send_message(message.chat.id,"🦜 says: Hello Apoorva")
    print(msg)
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
            bot.set_webhook(url='https://cloud-computing-assignment-pre.herokuapp.com/'+config.telegram_key)
            string='<!DOCTYPE html> <html> <head> <meta charset="utf-8"> <meta http-equiv="X-UA-Compatible" content="IE=edge"> <title>Cloud Computing</title> <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;700&display=swap" rel="stylesheet"/> <style> body{ height: 100vh; font-family: "Poppins", "Trebuchet MS", sans-serif; display: flex; align-items: center; justify-content: center; background: linear-gradient(to right top, #48bda7, #6ed4e4); } section{ height: 80vh; border-radius: 30px; width: 60%; padding: 20px; display: flex; align-items: center; justify-content: center; margin: 20px; z-index: 2; backdrop-filter: blur(80px); background: linear-gradient(to right bottom, rgba(255,255,255,0.7), rgba(255,255,255,0.3)); } .circle1, .circle2 { background: white; background: linear-gradient(to right bottom, rgba(255,255,255,0.8), rgba(255,255,255,0.3)); position: absolute; border-radius: 50%; } .circle1 { top: 5%; right: 15%; height: 150px; width: 150px; } .circle2 { bottom: 5%; left: 10%; height: 200px; width: 200px; } h3{ color: #32a873; } </style> </head> <body> <section> <center> <div> <h2>Bot created by</h2> <h3>Aarhon Joshua A</h3> <h3>Apoorva D</h3> <h3>Keshini P S</h3> <h3>Muhil Varsini S</h3> <h3>Sridhar Sriram</h3> </div> </center> </section> <div class="circle1"></div> <div class="circle2"></div> </body> </html>'
            return string, 200

    if __name__ == "__main__":
        server.debug=True
        server.run(host=config.host, port=config.port)
