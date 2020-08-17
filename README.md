<p align="center">
  <a href="https://github.com/Teraskull/GramControl"><img src="GramControl/icon.ico"></a>
</p>
<h1 align="center">
  GramControl
</h1>

<p align="center">
  IoT device based on the Python Socket module.
</p>

<p align="center">
  <a style="text-decoration:none" href="https://github.com/Teraskull/GramControl">
    <img src="https://img.shields.io/badge/Version-v4.0.0-brightgreen.svg?style=flat-square" alt="Version" />
  </a>
  <a style="text-decoration:none" href="https://github.com/Teraskull/GramControl">
    <img src="https://img.shields.io/badge/stability-unstable-yellow.svg?style=flat-square" alt="Stability" />
  </a>
  <a style="text-decoration:none" href="https://github.com/Teraskull/GramControl/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/Teraskull/GramControl?style=flat-square" alt="License" />
  </a>
</p>

**GramControl** is a Windows GUI client application for communicating with the GramBase server.\
**GramBase** is a [TCP/IP](https://docs.python.org/3/library/socket.html) Python server, that controls 3 separate outputs via the GPIO pins of a Raspberry Pi.

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

* [Environs](https://pypi.org/project/environs/) library
    ```bash
    > pip install environs
    ```
* [PyQt5](https://pypi.org/project/PyQt5/) GUI framework
    ```bash
    > pip install pyqt5
    ```


### Requirements for Raspberry Pi OS:

* Python 3.6+

* [Environs](https://pypi.org/project/environs/) library
    ```bash
    $ pip install environs
    ```
* [GPIO Zero](https://pypi.org/project/gpiozero/) library (Preinstalled on Raspberry Pi OS)
    ```bash
    $ pip install gpiozero
    ```

## Getting started


```bash
    $ git clone https://github.com/Teraskull/GramControl

    $ cd GramControl
```

Create an `.env` file in the root of both `GramBase` and `GramControl` directories, paste the following properties, and replace the `HOST` and `PORT` with your own values.

```python
HOST = 'Your Raspberry Pi IP address'
PORT = 'Any port >1024'
```


Generally, you don't need to configure anything in the scripts, everything should work after you setup your `.env` files.


## User manual

Once everything is set up, navigate to the directories and run the scripts.
First, run the server:
#### On Raspberry Pi OS:
  ```bash
$ cd /path/to/script/GramBase/
$ python server.py
  ```
Next, run the client application:
#### On Windows:
  ```bash
> cd /path/to/script/GramControl/
> python client.py
  ```

### Windows Application description

Functions of each button in the Windows application.

| Label | Switch |
| ------ | ------ |
| Light One | Toggle first pin. |
| Light Two | Toggle second pin. |
| Light Three | Toggle third pin. |
| Default Names | Use predefined names. |

## Functions
  - The preinstalled Python [JSON](https://docs.python.org/3/library/json.html) library is used to store variables. If the Client/Server is shut down while some GPIO pins are active, their state will be saved and will be restored next time you run the scripts.
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

