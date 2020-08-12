# GramControl

[![Version](https://img.shields.io/badge/Version-v5.5.2-brightgreen.svg?style=flat-square)](https://github.com/Teraskull/GramControl) [![Release](https://img.shields.io/badge/Release-Stable-blueviolet.svg?style=flat-square)](https://github.com/Teraskull/GramControl) [![License](https://img.shields.io/github/license/Teraskull/GramControl?style=flat-square)](https://github.com/Teraskull/GramControl/blob/master/LICENSE)

**GramControl** is a Windows GUI client application for communicating with the GramBase server.\
**GramBase** is a [Telegram](https://telegram.org/) Python bot, that acts as a server and controls 3 separate outputs via the GPIO pins of a Raspberry Pi.

### Hardware:
- Raspberry Pi to run the server (Tested on Model 3B+)
* Broadcom (BCM) pins used:
  * gpio_1 - BCM(17)
  * gpio_2 - BCM(27)
  * gpio_3 - BCM(22)
- SD Card with preinstalled [Raspbian Buster](https://www.raspberrypi.org/downloads/raspbian/) (Desktop or Lite)
- A Windows machine to run the application

### Software for Windows:
  - Python3 with pip - [Python 3.8](https://www.python.org/downloads/)
  - Telegram API library - [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)
  ```bash
> pip3 install pyTelegramBotAPI
  ```

  - PyQT5 GUI library - [PyQT5](https://riverbankcomputing.com/software/pyqt/download5)

  ```bash
> pip3 install pyqt5
  ```



### Software for Raspbian:

  - Python3 with pip
  ```bash
$ sudo apt update
$ sudo apt upgrade
$ sudo apt install python3
$ sudo apt install python3-pip
  ```
  - Telegram API library - [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)
  ```bash
$ sudo pip3 install pyTelegramBotAPI
  ```
  - GPIO control library (Is preinstalled on Raspberry Pi) - [GPIO Zero](https://gpiozero.readthedocs.io/en/stable/)
  ```bash
$ sudo apt install python3-gpiozero
  ```

## Getting started

To start, you need a [Telegram](https://telegram.org/) account.
Create two bots (Client and Server), disable their Group Privacy, allow Groups, and get their `TOKEN` using [@BotFather](https://core.telegram.org/bots#6-botfather).
As the Telegram API does not allow bots to communicate with each other directly, 
create a Telegram [channel](https://telegram.org/faq_channels) and add created bots to it.
Write down the channel `ID`. You can find the `ID` by writing in the channel and forwarding the message to [@getidsbot](https://t.me/getidsbot).\
*Note: The channel `ID` is in the **"Origin chat"** tab, not **"You"** tab.*

To be able to use the scripts with the bots, replace the `TOKEN` and the `ID` in the scripts with your own values.
```python
# Telegram values
token = 'TOKEN'
my_chat_id = ID
```
*Note: Make sure that `TOKEN` is inside quotation marks and `ID` is without them.*


Generally, you don't need to configure anything in the scripts, everything should work after you set your `TOKEN` and `ID` values.
Once everything is set up, navigate to the directories and run the scripts:
#### On Windows:
  ```bash
> cd /path/to/script/directory/
> python3 client.py
  ```
#### On Raspbian:
  ```bash
$ cd /path/to/script/directory/
$ python3 bot.py
  ```

## User manual

  - Find your bots, created with [@BotFather](https://telegram.me/BotFather), using the search bar.
  - Once found, press `START` on the bottom to initialize them.

### Telegram Keyboard Buttons

Functions of each button in the Windows application.

| Label | Switch |
| ------ | ------ |
| Light One | Toggle first pin. |
| Light Two | Toggle second pin. |
| Light Three | Toggle third pin. |
| Default Names | Use predefined names. |

## Functions
  - Bot uses a preinstalled Python [JSON library](https://docs.python.org/3/library/json.html) to store variables. If the Client/Server is shut down while some GPIO pins are active, their state will be saved and will be restored next time you run the scripts.
  - Bottom left bulb icon lights up if there is connection with the server.
  - Switch light and dark themes with the bottom left moon icon.

### To-dos
 - ✔ Switch to JSON serialization
 - Add more GPIO outputs(If needed)
 - Make GPIO pin state restoring optional
 - ✔ Add Settings menu
 - ✔ Add ability to edit button labels

## License

This software is available under the following licenses:

  * GPL-3.0

