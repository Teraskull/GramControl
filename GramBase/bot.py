# -*- coding: utf-8 -*-
from aiogram import Bot, Dispatcher, executor, types
from environs import Env, EnvValidationError
from aiogram.utils import exceptions
# from gpiozero import LEDBoard
from html import escape
import logging
import pickle
import os

# leds = LEDBoard(17, 27, 22)

__version__ = '4.0.0'

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
    CHANNEL_ID = env.int("CHANNEL_ID")
except EnvValidationError as env_error:
    logger.error(env_error)

bot = Bot(token=TELEGRAM_TOKEN, parse_mode="html")
dp = Dispatcher(bot)

# Values
chat_id_list = [CHANNEL_ID, MY_CHAT_ID]
server_online = 'Server online.'
server_offline = 'Server offline.'


# Handle errors. [BOT]
@dp.errors_handler()
async def errors_handler(update, error):
    logger.error(f'Update: {update}\n{error}')


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


# Handle the '/start' command.
@dp.message_handler(user_id=MY_CHAT_ID, chat_id=MY_CHAT_ID, commands=['start'])
async def info_message(message: types.Message):
    await message.answer(server_online)


# Handle messages. (Temporary lambda channel chat_id fix, issue #375)
@dp.edited_channel_post_handler(lambda message: message.chat.id in chat_id_list, content_types=['text'])
@dp.channel_post_handler(lambda message: message.chat.id in chat_id_list, content_types=['text'])
async def send_text(message: types.Message):
    new_text = escape(message.text.lower())

    if new_text == 'check_server':
        await message.answer(server_online)

    elif new_text == 'pin_1':
        room_1.toggle(0)

    elif new_text == 'pin_2':
        room_2.toggle(1)

    elif new_text == 'pin_3':
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


async def on_startup(dp):
    await bot.send_message(CHANNEL_ID, server_online)
    logger.info(f'[{__version__}] {server_online}')


async def on_shutdown():
    await bot.send_message(CHANNEL_ID, server_offline)
    # save_state()
    # leds.close()
    logger.info(f'[{__version__}] {server_offline}')
    logger.info(f'[{__version__}] Saved variables to gpio_state.pkl')


if __name__ == "__main__":
    while True:
        try:
            executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
            break
        finally:
            dp.loop.run_until_complete(on_shutdown())  # Call on_shutdown() from separate loop
