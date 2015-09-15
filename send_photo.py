import os
import telebot
import picamera
from random import randint
from fractions import Fraction

camera = picamera.PiCamera()
camera.framerate = Fraction(1, 6)
camera.shutter_speed = 6000000
camera.exposure_mode = 'off'
camera.iso = 800
bot = telebot.TeleBot("128892495:AAG0wYE55Vfi8QXutqPIuaquxiDPbxg-mtc")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['ambilgambar'])
def kirim_gambar(message):
	chat_id = message.chat.id
	filerand = 'gambar%s.jpg' % randint(1,5)
	camera.capture(filerand)
	photo = open(filerand, 'rb')
	bot.send_photo(chat_id, photo)
	os.remove(filerand)
	
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()