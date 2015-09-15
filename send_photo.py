import os
import time
import telebot
import picamera
from random import randint
from fractions import Fraction

bot = telebot.TeleBot("128892495:AAG0wYE55Vfi8QXutqPIuaquxiDPbxg-mtc")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['ambilgambar'])
def kirim_gambar(message):
	camera = picamera.PiCamera()
	camera.vflip = True
	chat_id = message.chat.id
	filerand = 'gambar%s.jpg' % randint(1,5)
	time.sleep(1)
	camera.capture(filerand)
	photo = open(filerand, 'rb')
	bot.send_photo(chat_id, photo)
	os.remove(filerand)
	camera.close()

@bot.message_handler(commands=['ambilgambarm'])
def kirim_gambar(message):
	camera = picamera.PiCamera()
	camera.vflip = True
	camera.framerate = Fraction(1, 6)
	camera.shutter_speed = 6000000
	camera.exposure_mode = 'off'
	camera.iso = 800
	chat_id = message.chat.id
	filerand = 'gambar%s.jpg' % randint(1,5)
	camera.capture(filerand)
	photo = open(filerand, 'rb')
	bot.send_photo(chat_id, photo)
	os.remove(filerand)
	camera.close()

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()