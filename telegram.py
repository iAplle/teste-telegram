from flask import Flask, request, render_template, jsonify
import pyautogui
import os
import telebot
import requests
from telebot import types
import time
import sys

token = '6298765557:AAHqoZkNpcef5YdUngy2QXjQW-hFgeSk8RA'
chat_id = '-1002026552071'
chat_idScreenshot = '-4127227129'
chat_idfoto = '-4086617995'
chat_notificacoes = '-4099466791'

bot = telebot.TeleBot(token)
bot.remove_webhook()

WEBHOOK_URL_BASE = public_url
WEBHOOK_URL_PATH = "/callback"

bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH, timeout=300)

app = Flask(__name__)

@app.route(WEBHOOK_URL_PATH, methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode("utf-8"))
    bot.process_new_updates([update])
    return '', 200

@bot.message_handler(commands=['keyboard'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton('Tirar screenshot da tela')
    item2 = types.KeyboardButton('Screenshot Admins')
    item3 = types.KeyboardButton('Screenshot status')
    item4 = types.KeyboardButton('Reconectar ao servidor')
    item5 = types.KeyboardButton('Remover Colisao')
    item6 = types.KeyboardButton('Tirar screenshot do jogo')
    item7 = types.KeyboardButton('/apd')
    markup.add(item1, item2, item3, item4, item5, item6, item7)
    bot.reply_to(message, "Escolha uma opção:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Tirar screenshot da tela")
def send_foto(message):
    bot.reply_to(message, "Tirando screenshot da tela!")
    screenshot_tela = pyautogui.screenshot()
    bot.send_photo(chat_idfoto, screenshot_tela)

@bot.message_handler(func=lambda message: message.text == "Screenshot Admins")
def send_admin(message):
    bot.reply_to(message, "Tirando screenshot dos administradores online!")
    pyautogui.press('t')
    time.sleep(1)
    pyautogui.write('/admins')
    pyautogui.press('enter')
    time.sleep(1)
    screenshot_admin = pyautogui.screenshot()
    bot.send_photo(chat_idfoto, screenshot_admin)
    time.sleep(2)
    pyautogui.press('esc')

@bot.message_handler(func=lambda message: message.text == "Screenshot status")
def send_status(message):
    bot.reply_to(message, "Tirando screenshot do status!")
    pyautogui.press('t')
    time.sleep(1)
    pyautogui.write('/status')
    pyautogui.press('enter')
    time.sleep(1)
    screenshot_status = pyautogui.screenshot()
    bot.send_photo(chat_idfoto, screenshot_status)

@bot.message_handler(func=lambda message: message.text == "Reconectar ao servidor")
def send_recon(message):
    bot.reply_to(message, "Reconectando ao servidor!")
    pyautogui.press('t')
    time.sleep(1)
    pyautogui.write('/recon')
    pyautogui.press('enter')
    time.sleep(1)
    screenshot_recon = pyautogui.screenshot()
    bot.send_photo(chat_idfoto, screenshot_recon)

@bot.message_handler(func=lambda message: message.text == "Remover Colisao")
def remove_colision(message):
    bot.reply_to(message, "Removendo colisao")
    pyautogui.press('t')
    time.sleep(1)
    pyautogui.write('/nocols')
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('down', presses=5)
    time.sleep(1)
    pyautogui.press('enter')
    screenshot_colision = pyautogui.screenshot()
    bot.send_photo(chat_idfoto, screenshot_colision)
    time.sleep(1)
    pyautogui.press('esc')

@bot.message_handler(func=lambda message: True)
def received_messages(message):
    received_message = message.text
    bot.reply_to(message, "Enviando sua mensagem!")
    pyautogui.press('t')
    time.sleep(1)
    pyautogui.write(message.text)
    pyautogui.press('enter')
    time.sleep(1)
    screenshot_message = pyautogui.screenshot()
    bot.send_photo(chat_idfoto, screenshot_message)

if __name__ == '__main__':
    app.run(debug=True)