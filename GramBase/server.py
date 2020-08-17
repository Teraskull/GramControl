# -*- coding: utf-8 -*-
from environs import Env, EnvValidationError
# from gpiozero import LEDBoard
from threading import Thread
import logging
import pickle
import socket
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
    HOST = env("HOST")
    PORT = env.int("PORT")
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


class ServerThread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((HOST, PORT))
            s.listen(1)
            while True:
                print("[!] Server: Waiting for connection from TCP client...")
                conn, (ip, port) = s.accept()
                # logger.info(f'[{__version__}] [+] Client {ip}:{port} connected.')
                print(f'[+] Client {ip}:{port} connected.')
                while True:
                    try:
                        data = conn.recv(1024).decode()
                        if not data:
                            pass
                        if data == 'check_server':
                            conn.send(server_online.encode())
                        elif data == 'pin_1':
                            room_1.toggle(0)
                        elif data == 'pin_2':
                            room_2.toggle(1)
                        elif data == 'pin_3':
                            room_3.toggle(2)
                    except ConnectionResetError:
                        # logger.info(f'[{__version__}] [-] Client {ip}:{port} disconnected.')
                        print(f'[-] Client {ip}:{port} disconnected.')
                        break


if __name__ == "__main__":
    try:
        serverThread = ServerThread()
        serverThread.run()
    finally:
        # leds.close()
        pass
