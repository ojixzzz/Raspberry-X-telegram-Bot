import telebot
import picamera
from StringIO import StringIO

camera = picamera.PiCamera()
bot = telebot.TeleBot("128892495:AAG0wYE55Vfi8QXutqPIuaquxiDPbxg-mtc")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['ambilgambar'])
def kirim_gambar(message):
	chat_id = message.chat.id
	gambarnya = StringIO()
	camera.capture(gambarnya, format='jpeg')
	bot.send_photo(chat_id, gambarnya)
	bot.send_photo(chat_id, "FILEID")
	
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()