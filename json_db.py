# -*- coding: utf-8 -*-

import json
import os


class Database:
	def __init__(self):
		super().__init__()

	def default_json(self):
		data = {
			'home': {
				'roomName': 'Default Room',
				'light1': 'Light One',
				'light2': 'Light Two',
				'light3': 'Light Three',
				'button1': False,
				'button2': False,
				'button3': False
			},
			'settings': {
				'button1': False,
			},
			'sidebar': {
				'mode': False,
			}
		}
		return data

	def save_database(self, data):
		with open('database.json', 'w') as save_file:
			json.dump(data, save_file, indent=4)

	def read_database(self):
		if os.path.isfile('database.json'):
			try:
				with open('database.json', 'r') as load_file:
					data = json.load(load_file)
			except (ValueError, TypeError) as e:
				data = self.default_json()
				self.save_database(data)
		else:
			data = self.default_json()
			self.save_database(data)
		return data


# Basic Usage

# class MainWindow():
# 	def ui_setup(self):
# 		db = Database()
# 		data = db.read_database()
# 		data['home']['light1'] = 'fgeonpo'
# 		print(data['home']['light1'])
# 		db.save_database(data)
#
#
# test = MainWindow()
# test.ui_setup()
