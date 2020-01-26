# -*- coding: utf-8 -*-

"""
GramControl Client
PyQt5 GUI
Last edited: 26 January 2020
"""

from PyQt5.QtCore import Qt, QSize, QRect
from PyQt5.QtWidgets import QPushButton, QMainWindow, QWidget, QFrame, QLabel, QLineEdit
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon, QFont, QPixmap


class MainWindowUI(QMainWindow):
    def __init__(self):
        super(MainWindowUI, self).__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowTitle('GramControl Client')
        self.setWindowIcon(QIcon('icon.ico'))
        self.setFixedSize(460, 415)
        self.img_on = QPixmap(':/button/on')
        self.img_off = QPixmap(':/button/off')

    def ui_setup(self):
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Home frame ################################################
        self.frame_home = QFrame(self.central_widget)
        self.frame_home.setGeometry(QRect(51, 0, 409, 415))

        # Room frame
        self.frame_0 = QFrame(self.frame_home)
        self.frame_0.setGeometry(QRect(0, 0, 409, 51))

        self.text_0 = QLineEdit(self.frame_0)
        self.text_0.setGeometry(QRect(0, 0, 409, 51))
        self.text_0.setFrame(False)
        self.text_0.setMaxLength(20)
        self.text_0.setAlignment(Qt.AlignCenter)
        self.text_0.setReadOnly(True)
        self.text_0.setText('Default Room')

        # Light 1 frame
        self.frame_1 = QFrame(self.frame_home)
        self.frame_1.setGeometry(QRect(0, 51, 409, 91))

        self.text_1 = QLineEdit(self.frame_1)
        self.text_1.setGeometry(QRect(10, 0, 310, 91))
        self.text_1.setFrame(False)
        self.text_1.setMaxLength(20)
        self.text_1.setReadOnly(True)
        self.text_1.setText('Light One')

        self.switch_1 = QPushButton(self.frame_1)
        self.switch_1.setGeometry(QRect(340, 30, 51, 31))
        self.switch_1.setIconSize(QSize(51, 31))
        self.switch_1.setCheckable(True)
        self.switch_1.setStyleSheet("border: none;")
        self.switch_1.setIcon(QIcon(self.img_off))
        self.switch_1.setMask(self.img_off.mask())

        # Light 2 frame
        self.frame_2 = QFrame(self.frame_home)
        self.frame_2.setGeometry(QRect(0, 142, 409, 91))

        self.text_2 = QLineEdit(self.frame_2)
        self.text_2.setGeometry(QRect(10, 0, 310, 91))
        self.text_2.setFrame(False)
        self.text_2.setMaxLength(20)
        self.text_2.setReadOnly(True)
        self.text_2.setText('Light Two')

        self.switch_2 = QPushButton(self.frame_2)
        self.switch_2.setGeometry(QRect(340, 30, 51, 31))
        self.switch_2.setIconSize(QSize(51, 31))
        self.switch_2.setCheckable(True)
        self.switch_2.setStyleSheet("border: none;")
        self.switch_2.setIcon(QIcon(self.img_off))
        self.switch_2.setMask(self.img_off.mask())

        # Light 3 frame
        self.frame_3 = QFrame(self.frame_home)
        self.frame_3.setGeometry(QRect(0, 233, 409, 91))

        self.text_3 = QLineEdit(self.frame_3)
        self.text_3.setGeometry(QRect(10, 0, 310, 91))
        self.text_3.setFrame(False)
        self.text_3.setMaxLength(20)
        self.text_3.setReadOnly(True)
        self.text_3.setText('Light Three')

        self.switch_3 = QPushButton(self.frame_3)
        self.switch_3.setGeometry(QRect(340, 30, 51, 31))
        self.switch_3.setIconSize(QSize(51, 31))
        self.switch_3.setCheckable(True)
        self.switch_3.setStyleSheet("border: none;")
        self.switch_3.setIcon(QIcon(self.img_off))
        self.switch_3.setMask(self.img_off.mask())

        # Edit frame
        self.frame_4 = QFrame(self.frame_home)
        self.frame_4.setGeometry(QRect(0, 324, 409, 91))

        # Settings Frame ############################################
        self.frame_settings = QFrame(self.central_widget)
        self.frame_settings.setGeometry(QRect(51, 0, 409, 415))
        self.frame_settings.hide()

        # Title frame
        self.frame_title = QFrame(self.frame_settings)
        self.frame_title.setGeometry(QRect(0, 0, 409, 51))

        self.settings_title = QLabel(self.frame_title)
        self.settings_title.setGeometry(QRect(0, 0, 409, 51))
        self.settings_title.setText('Settings')
        self.settings_title.setAlignment(Qt.AlignCenter)

        # Controls frame
        self.frame_controls = QFrame(self.frame_settings)
        self.frame_controls.setGeometry(QRect(0, 51, 409, 415))

        self.settings_label_1 = QLabel(self.frame_controls)
        self.settings_label_1.setGeometry(QRect(12, 0, 308, 91))
        self.settings_label_1.setText('Default names')

        self.s_switch_1 = QPushButton(self.frame_controls)
        self.s_switch_1.setGeometry(QRect(340, 30, 51, 31))
        self.s_switch_1.setIconSize(QSize(51, 31))
        self.s_switch_1.setCheckable(True)
        self.s_switch_1.setStyleSheet("border: none")
        self.s_switch_1.setIcon(QIcon(self.img_off))
        self.s_switch_1.setMask(self.img_off.mask())

        # Info Frame ################################################

        self.frame_info = QFrame(self.central_widget)
        self.frame_info.setGeometry(QRect(51, 0, 409, 415))
        self.frame_info.hide()

        # Title frame
        self.frame_info_top = QFrame(self.frame_info)
        self.frame_info_top.setGeometry(QRect(0, 0, 409, 51))

        self.info_title = QLabel(self.frame_info_top)
        self.info_title.setGeometry(QRect(0, 0, 409, 51))
        self.info_title.setText('Information')
        self.info_title.setAlignment(Qt.AlignCenter)

        # Credits frame
        self.frame_credits = QFrame(self.frame_info)
        self.frame_credits.setGeometry(QRect(0, 51, 409, 415))

        self.credits_label_1 = QLabel(self.frame_credits)
        self.credits_label_1.setGeometry(QRect(0, 0, 409, 150))
        credits_text = '''
GramControl Client

Interface - Katarzyna Firmanty
Design - Marceli Wielopolski
Backend - Anton Grouchtchak
'''
        self.credits_label_1.setText(credits_text)
        self.credits_label_1.setFont(QFont('century gothic', 12, 50))

        self.credits_label_2 = QLabel(self.frame_credits)
        self.credits_label_2.setGeometry(QRect(0, 150, 409, 30))
        self.credits_label_2.setOpenExternalLinks(True)
        self.credits_label_2.setFont(QFont('century gothic', 12, 50))
        self.credits_label_2.setAlignment(Qt.AlignCenter)

        self.s_logo = QLabel(self.frame_credits)
        self.s_logo.setGeometry(QRect(96, 322, 218, 25))
        self.s_logo.setStyleSheet("border-image: url(:/button/16.png);")

        self.s_version = QLabel(self.frame_credits)
        self.s_version.setGeometry(QRect(355, 347, 50, 16))
        self.s_version.setFont(QFont('century gothic', 10, 50))
        self.s_version.setText('v5.5.2')
        self.s_version.setAlignment(Qt.AlignRight)

        # Sidebar frame #############################################
        self.frame_sidebar = QFrame(self.central_widget)
        self.frame_sidebar.setGeometry(QRect(0, 0, 51, 415))
        self.frame_sidebar.setStyleSheet("background-color: rgb(52, 52, 52);")

        self.home_button = QPushButton(self.frame_sidebar)
        self.home_button.setGeometry(QRect(0, 0, 51, 51))
        self.home_button.setStyleSheet("background-color: rgb(35, 35, 35); border: none;")
        self.home_button.setIcon(QIcon(':/button/6.png'))
        self.home_button.setIconSize(QSize(28, 23))

        self.settings_button = QPushButton(self.frame_sidebar)
        self.settings_button.setGeometry(QRect(0, 51, 51, 51))
        self.settings_button.setStyleSheet("background-color: none; border: none;")
        self.settings_button.setIcon(QIcon(':/button/11.png'))
        self.settings_button.setIconSize(QSize(27, 27))

        self.info_button = QPushButton(self.frame_sidebar)
        self.info_button.setGeometry(QRect(0, 102, 51, 51))
        self.info_button.setStyleSheet("background-color: none; border: none;")
        self.info_button.setIcon(QIcon(':/button/info'))
        self.info_button.setIconSize(QSize(26, 26))

        self.edit_button = QPushButton(self.frame_sidebar)
        self.edit_button.setGeometry(QRect(0, 153, 51, 51))
        self.edit_button.setCheckable(True)
        self.edit_button.setStyleSheet("background-color: none; border: none;")
        self.edit_button.setIcon(QIcon(':/button/write'))
        self.edit_button.setIconSize(QSize(29, 32))

        self.mode_button = QPushButton(self.frame_sidebar)
        self.mode_button.setGeometry(QRect(0, 313, 51, 51))
        self.mode_button.setCheckable(True)
        self.mode_button.setStyleSheet("background-color: none; border: none;")
        self.mode_button.setIcon(QIcon(':/button/moon'))
        self.mode_button.setIconSize(QSize(25, 25))

        self.status_icon = QPushButton(self.frame_sidebar)
        self.status_icon.setGeometry(QRect(0, 364, 51, 51))
        self.status_icon.setStyleSheet("background-color: none; border: none;")
        self.status_icon.setIcon(QIcon(':/button/13.png'))
        self.status_icon.setIconSize(QSize(18, 26))
