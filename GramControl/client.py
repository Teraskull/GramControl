# -*- coding: utf-8 -*-

import sys
import img_res
from json_db import Database
from ui_layout import MainWindowUI
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QSize, QRect
import threading
import telebot


# Telegram values
TOKEN = 'TOKEN'
my_chat_id = ID

bot = telebot.AsyncTeleBot(TOKEN)
bot.send_message(my_chat_id, 'check_server')


@bot.channel_post_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Server offline.':
        ui.status_icon.setIcon(QIcon(':/button/13.png'))
    else:
        ui.status_icon.setIcon(QIcon(':/button/12.png'))


def botd():
    bot.infinity_polling(True)


def create_thread():
    bot_daemon = threading.Thread(target=botd)
    bot_daemon.setDaemon(True)
    bot_daemon.start()


class Logic():
    def __init__(self):
        self.db = Database()
        self.data = self.db.read_database()

    def logic_setup(self):
        if self.data['home']['button1']:
            ui.switch_1.toggle()
            ui.switch_1.setIcon(QIcon(ui.img_on))
        if self.data['home']['button2']:
            ui.switch_2.toggle()
            ui.switch_2.setIcon(QIcon(ui.img_on))
        if self.data['home']['button3']:
            ui.switch_3.toggle()
            ui.switch_3.setIcon(QIcon(ui.img_on))
        if self.data['settings']['button1']:
            ui.s_switch_1.toggle()
            ui.s_switch_1.setIcon(QIcon(ui.img_on))
        if self.data['sidebar']['mode']:
            ui.mode_button.toggle()
            ui.mode_button.setIcon(QIcon(':/button/sun'))
            ui.mode_button.setIconSize(QSize(27, 27))

        self.set_names()
        self.set_lightmode()

        ui.switch_1.clicked.connect(self.toggle_switch_1)
        ui.switch_2.clicked.connect(self.toggle_switch_2)
        ui.switch_3.clicked.connect(self.toggle_switch_3)
        ui.home_button.clicked.connect(lambda: self.toggle_window(0))
        ui.settings_button.clicked.connect(lambda: self.toggle_window(1))
        ui.info_button.clicked.connect(lambda: self.toggle_window(2))
        ui.edit_button.clicked.connect(self.edit_mode)
        ui.s_switch_1.clicked.connect(self.set_names)
        ui.mode_button.clicked.connect(self.set_lightmode)

    def set_lightmode(self):
        light = (236, 240, 241)
        dark = (35, 35, 35)
        if ui.mode_button.isChecked():
            self.data['sidebar']['mode'] = True
            ui.mode_button.setIcon(QIcon(':/button/sun'))
            ui.mode_button.setIconSize(QSize(27, 27))
            ui.frame_settings.setStyleSheet(f"color: rgb{dark}; background-color: rgb{light};")
            ui.frame_home.setStyleSheet(f"color: rgb{dark}; background-color: rgb{light};")
            ui.frame_info.setStyleSheet(f"color: rgb{dark}; background-color: rgb{light};")
            ui.credits_label_2.setText(f'''<a href="https://github.com/Teraskull/GramControl">
                                       <span style="color:rgb{dark};">Github</a>''')
        else:
            self.data['sidebar']['mode'] = False
            ui.mode_button.setIcon(QIcon(':/button/moon'))
            ui.mode_button.setIconSize(QSize(25, 25))
            ui.frame_settings.setStyleSheet(f"color: rgb{light}; background-color: rgb{dark};")
            ui.frame_home.setStyleSheet(f"color: rgb{light}; background-color: rgb{dark};")
            ui.frame_info.setStyleSheet(f"color: rgb{light}; background-color: rgb{dark};")
            ui.credits_label_2.setText(f'''<a href="https://github.com/Teraskull/GramControl">
                                       <span style="color:rgb{light};">Github</a>''')
        self.db.save_database(self.data)

    def set_names(self):
        if ui.s_switch_1.isChecked():
            self.data['settings']['button1'] = True
            ui.s_switch_1.setIcon(QIcon(ui.img_on))
            ui.edit_button.hide()
            self.set_default()
        else:
            self.data['settings']['button1'] = False
            ui.s_switch_1.setIcon(QIcon(ui.img_off))
            ui.edit_button.show()
            ui.text_0.setText(self.data['home']['roomName'])
            ui.text_1.setText(self.data['home']['light1'])
            ui.text_2.setText(self.data['home']['light2'])
            ui.text_3.setText(self.data['home']['light3'])
        self.db.save_database(self.data)

    def save_names(self):
        self.data['home']['roomName'] = ui.text_0.text()
        self.data['home']['light1'] = ui.text_1.text()
        self.data['home']['light2'] = ui.text_2.text()
        self.data['home']['light3'] = ui.text_3.text()
        self.db.save_database(self.data)

    def set_default(self):
        ui.text_0.setText('Default Room')
        ui.text_1.setText('Light One')
        ui.text_2.setText('Light Two')
        ui.text_3.setText('Light Three')

    def toggle_window(self, mode):
        if mode == 0:  # home
            ui.edit_button.setEnabled(True)
            ui.frame_home.show()
            ui.frame_settings.hide()
            ui.frame_info.hide()
            ui.home_button.setStyleSheet("background-color: rgb(35, 35, 35); border: none;")
            ui.settings_button.setStyleSheet("background-color: none; border: none;")
            ui.info_button.setStyleSheet("background-color: none; border: none;")
        elif mode == 1:  # settings
            if ui.edit_button.isChecked():
                ui.edit_button.setChecked(False)
                self.edit_mode()
            ui.edit_button.setEnabled(False)
            ui.frame_settings.show()
            ui.frame_home.hide()
            ui.frame_info.hide()
            ui.home_button.setStyleSheet("background-color: none; border: none;")
            ui.settings_button.setStyleSheet("background-color: rgb(35, 35, 35); border: none;")
            ui.info_button.setStyleSheet("background-color: none; border: none;")
        elif mode == 2:  # Info
            if ui.edit_button.isChecked():
                ui.edit_button.setChecked(False)
                self.edit_mode()
            ui.edit_button.setEnabled(False)
            ui.frame_info.show()
            ui.frame_home.hide()
            ui.frame_settings.hide()
            ui.home_button.setStyleSheet("background-color: none; border: none;")
            ui.settings_button.setStyleSheet("background-color: none; border: none;")
            ui.info_button.setStyleSheet("background-color: rgb(35, 35, 35); border: none;")

    def edit_mode(self):
        if ui.edit_button.isChecked():
            ui.edit_button.setIcon(QIcon(':/button/17.png'))
            ui.text_0.setReadOnly(False)
            ui.text_1.setReadOnly(False)
            ui.text_2.setReadOnly(False)
            ui.text_3.setReadOnly(False)
            ui.switch_1.setEnabled(False)
            ui.switch_2.setEnabled(False)
            ui.switch_3.setEnabled(False)
            ui.switch_1.setStyleSheet("QPushButton{border-image: url(:/button/19);}\n"
                                      "QPushButton:checked{border-image: url(:/button/18);}")
            ui.switch_2.setStyleSheet("QPushButton{border-image: url(:/button/19);}\n"
                                      "QPushButton:checked{border-image: url(:/button/18);}")
            ui.switch_3.setStyleSheet("QPushButton{border-image: url(:/button/19);}\n"
                                      "QPushButton:checked{border-image: url(:/button/18);}")
        else:
            self.save_names()
            ui.edit_button.setIcon(QIcon(':/button/write'))
            ui.text_0.setReadOnly(True)
            ui.text_1.setReadOnly(True)
            ui.text_2.setReadOnly(True)
            ui.text_3.setReadOnly(True)
            ui.switch_1.setEnabled(True)
            ui.switch_2.setEnabled(True)
            ui.switch_3.setEnabled(True)
            ui.switch_1.setStyleSheet("QPushButton{border-image: url(:/button/off);}\n"
                                      "QPushButton:checked{border-image: url(:/button/on);}")
            ui.switch_2.setStyleSheet("QPushButton{border-image: url(:/button/off);}\n"
                                      "QPushButton:checked{border-image: url(:/button/on);}")
            ui.switch_3.setStyleSheet("QPushButton{border-image: url(:/button/off);}\n"
                                      "QPushButton:checked{border-image: url(:/button/on);}")

    def toggle_switch_1(self):
        if ui.switch_1.isChecked():
            self.data['home']['button1'] = True
            ui.switch_1.setIcon(QIcon(ui.img_on))
        else:
            self.data['home']['button1'] = False
            ui.switch_1.setIcon(QIcon(ui.img_off))
        self.db.save_database(self.data)
        # bot.send_message(my_chat_id, 'pin_1')

    def toggle_switch_2(self):
        if ui.switch_2.isChecked():
            self.data['home']['button2'] = True
            ui.switch_2.setIcon(QIcon(ui.img_on))
        else:
            self.data['home']['button2'] = False
            ui.switch_2.setIcon(QIcon(ui.img_off))
        self.db.save_database(self.data)
        # bot.send_message(my_chat_id, 'pin_2')

    def toggle_switch_3(self):
        if ui.switch_3.isChecked():
            self.data['home']['button3'] = True
            ui.switch_3.setIcon(QIcon(ui.img_on))
        else:
            self.data['home']['button3'] = False
            ui.switch_3.setIcon(QIcon(ui.img_off))
        self.db.save_database(self.data)
        # bot.send_message(my_chat_id, 'pin_3')


if __name__ == '__main__':
    create_thread()
    app = QApplication(sys.argv)
    app.setFont(QFont('century gothic', 20, 50))
    ui = MainWindowUI()
    ui.ui_setup()
    ui.show()
    logic = Logic()
    logic.logic_setup()
    sys.exit(app.exec_())
