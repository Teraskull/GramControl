# -*- coding: utf-8 -*-
from environs import Env, EnvValidationError
# from gpiozero import LEDBoard
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

logger = logging.getLogger('dev')
logger.setLevel(logging.DEBUG)

env = Env()
env.read_env()
try:
    DEV = env.bool("DEV")
except EnvValidationError as env_error:
    logger.error(env_error)


# Values
server_online = 'Server online.'
server_offline = 'Server offline.'


class Button:
    def __init__(self, state):
        self.state = state

    def toggle(self, i):
        # leds[i].toggle()
        self.state = not self.state  # If LED ON, then turn it OFF, and vice versa
        # save_state()
        return self.state


# Class objects
room_1 = Button(False)
room_2 = Button(False)
room_3 = Button(False)


async def send_text(message):
    new_text = message.lower()

    if new_text == 'check_server':
        logger.info(new_text)

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
    pass
    # save_state()


if __name__ == "__main__":
    try:
        logger.info(f'[{__version__}] {server_online}')
    finally:
        # save_state()
        # leds.close()
        logger.info(f'[{__version__}] {server_offline}')
        logger.info(f'[{__version__}] Saved variables to gpio_state.pkl')
