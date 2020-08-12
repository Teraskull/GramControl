# -*- coding: utf-8 -*-
#
# GramControl Bot - @GramControlBot
#
# Anton Grouchtchak 2020

import config
import telebot
import pickle
import os
import atexit
from telebot import types
from aiogram import Bot, Dispatcher, executor, types
from environs import Env, EnvValidationError
from aiogram.utils import exceptions
import logging
# from gpiozero import LEDBoard

# leds = LEDBoard(17, 27, 22)

logging.basicConfig(handlers=[
                    logging.StreamHandler()
                    ],
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y.%m.%d %H:%M:%S',
                    level=logging.INFO
                    )

aio_logger = logging.getLogger("aiogram")
aio_logger.setLevel(logging.ERROR)
logger = logging.getLogger('dev')
logger.setLevel(logging.DEBUG)

env = Env()
env.read_env()
try:
    TELEGRAM_TOKEN = env("TELEGRAM_TOKEN")
    MY_CHAT_ID = env.int("MY_CHAT_ID")
    BOT_DEV = env.bool("BOT_DEV")
except EnvValidationError as env_error:
    logger.error(env_error)

bot = telebot.TeleBot(config.token)
# bot = Bot(token=TELEGRAM_TOKEN, parse_mode="html")
# dp = Dispatcher(bot)

# Values
my_chat_id = config.my_chat_id
info_text = config.info_text
server_online = 'Server online.'
server_offline = 'Server offline.'


def exit_handler():
    bot.send_message(my_chat_id, server_offline)
    # save_state()
    print(' Interrupted by user')
    print(' Saved variables to gpio_state.pkl')
    # leds.close()


class Button:
    def __init__(self, state):
        self.state = state

    def toggle(self, i):
        # leds[i].toggle()
        self.state = not self.state  # If LED ON, then turn it OFF, and vice versa
        save_state()
        return self.state


# Class objects
room_1 = Button(False)
room_2 = Button(False)
room_3 = Button(False)


# Send text 'Server online.' when connected.
bot.send_message(my_chat_id, server_online)


# Handle the '/start' command.
@bot.message_handler(commands=['start'])
def welcome_message(message):
    if message.chat.id == 212947118:
        print(server_online)


# Handle text messages.
@bot.channel_post_handler(content_types=['text'])
def send_text(message):
    if message.chat.id == my_chat_id:

        my_text = message.text.lower()

        if my_text == 'check_server':
            bot.send_message(my_chat_id, server_online)

        elif my_text == 'pin_1':
            room_1.toggle(0)

        elif my_text == 'pin_2':
            room_2.toggle(1)

        elif my_text == 'pin_3':
            room_3.toggle(2)


# Save state of pins
def save_state():
    with open('gpio_state.pkl', 'wb') as save_file:
        pickle.dump([room_1.state, room_2.state, room_3.state], save_file)


# If file gpio_state.pkl exists, load values from it.
if os.path.isfile('gpio_state.pkl'):
    with open('gpio_state.pkl', 'rb') as load_file:
        room_1.state, room_2.state, room_3.state = pickle.load(load_file)

# If file gpio_state.pkl does not exist, load default values.
else:
    save_state()


if __name__ == '__main__':
    try:
        bot.infinity_polling(True)
    finally:
        atexit.register(exit_handler)
