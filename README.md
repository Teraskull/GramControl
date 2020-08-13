<p align="center">
  <a href="https://github.com/Teraskull/GramControl"><img src="GramControl/icon.ico"></a>
</p>
<h1 align="center">
  GramControl
</h1>

<p align="center">
  IoT device based on the Telegram API.
</p>

<p align="center">
  <a style="text-decoration:none" href="https://github.com/Teraskull/GramControl">
    <img src="https://img.shields.io/badge/Version-v4.0.0-brightgreen.svg?style=flat-square" alt="Version" />
  </a>
  <a style="text-decoration:none" href="https://github.com/Teraskull/GramControl">
    <img src="https://img.shields.io/badge/Release-Stable-blueviolet.svg?style=flat-square" alt="Release" />
  </a>
  <a style="text-decoration:none" href="https://github.com/Teraskull/GramControl/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/Teraskull/GramControl?style=flat-square" alt="License" />
  </a>
</p>

**GramControl** is a Windows GUI client application for communicating with the GramBase server.\
**GramBase** is a [Telegram](https://telegram.org/) Python bot, that acts as a server and controls 3 separate outputs via the GPIO pins of a Raspberry Pi.

### Hardware:
- Raspberry Pi to run the server (Tested on Model 3B+)
* Broadcom (BCM) pins used:
  * gpio_1 - BCM(17)
  * gpio_2 - BCM(27)
  * gpio_3 - BCM(22)
- SD Card with preinstalled [Raspberry Pi OS](https://www.raspberrypi.org/downloads/raspberry-pi-os/) (Desktop or Lite)
- A Windows machine to run the application


## Requirements for Windows:

* Python 3.6+

* [Aiogram](https://github.com/aiogram/aiogram) library
    ```console
    $ pip install aiogram
    ```
* [PyQt5](https://pypi.org/project/PyQt5/) GUI framework
    ```console
    $ pip install pyqt5
    ```


### Requirements for Raspberry Pi OS:

* Python 3.6+

* [Aiogram](https://github.com/aiogram/aiogram) library
    ```console
    $ pip install aiogram
    ```
* [GPIO Zero](https://pypi.org/project/gpiozero/) library (Preinstalled on Raspberry Pi OS)
    ```console
    $ pip install gpiozero
    ```

## Getting started

To start, you need a [Telegram](https://telegram.org/) account.
Create two bots (Client and Server), disable their Group Privacy, allow Groups, and get their `TOKEN` using [@BotFather](https://core.telegram.org/bots#6-botfather).
As the Telegram API does not allow bots to communicate with each other directly, 
create a Telegram [channel](https://telegram.org/faq_channels) and add created bots to it.
Write down the channel `ID`. You can find the `ID` by writing in the channel and forwarding the message to [@my_id_bot](https://t.me/my_id_bot).\
*Note: You should receive a reply like "This channel's ID is `-1234567890`"*\
Repeat the process with your own `CHAT_ID`.

To be able to use the scripts with the bots, create an `.env` file, paste the following properties, and replace the `TOKEN`, `CHAT_ID` and the `ID` with your own values.

```python
TELEGRAM_TOKEN = "TOKEN"
MY_CHAT_ID = "CHAT_ID"
CHANNEL_ID = "ID"
```


Generally, you don't need to configure anything in the scripts, everything should work after you setup your `.env` file.
Once everything is set up, navigate to the directories and run the scripts:
#### On Windows:
  ```console
> cd /path/to/script/directory/
> python client.py
  ```
#### On Raspberry Pi OS:
  ```console
$ cd /path/to/script/directory/
$ python bot.py
  ```

## User manual

  - Find your bots, created with [@BotFather](https://telegram.me/BotFather), using the search bar.
  - Once found, press `START` on the bottom to initialize them.

### Windows Application description

Functions of each button in the Windows application.

| Label | Switch |
| ------ | ------ |
| Light One | Toggle first pin. |
| Light Two | Toggle second pin. |
| Light Three | Toggle third pin. |
| Default Names | Use predefined names. |

## Functions
  - Bot uses a preinstalled Python [JSON](https://docs.python.org/3/library/json.html) library to store variables. If the Client/Server is shut down while some GPIO pins are active, their state will be saved and will be restored next time you run the scripts.
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

