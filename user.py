#!/usr/bin/env python3

# Main user charactrer class and methods

import random, time
import creatures

class Prisoner(object):
	
	def __init__(self, name = 'Unknown', hp = 20, escapeStatus = False, difficulty = 'medium'):
		self.name = name
		if difficulty.upper() == 'easy'.upper():
			hp = 40
		elif difficulty.upper() == 'medium'.upper():
			hp = 20
		else:
			hp = 10
		self.hp = hp
		self.escapeStatus = escapeStatus
		self.difficulty = difficulty

# Combat function for creature encounters

	def combat(self,  monster = None):
		while monster.hp > 0:
			if self.hp <= 0:
				print('You have died to a',monster.name)
				break
			elif monster.hp > 0:
				attack = random.randint(1,6)
				print('You strike at the',monster.name,'dealing',attack,'damage')
				time.sleep(3)
				monster.hp -= attack
				if monster.hp > 0:
					print('The',monster.name, 'takes a beating. It has', monster.hp, 'health remaining')
					time.sleep(3)
					self.hp -= monster.attack
					print('The', monster.name, 'hits you for', monster.attack, 'damage; your health is now',self.hp)
					time.sleep(3)
				else:
					print('The', monster.name, 'is dead')
					break
			else:
				break

# Functions to set self variables

	def setHP(self, new_hp = None):
		self.hp = new_hp

	def setescapeStatus(self, escapeStatus = False):
		self.escapeStatus = escapeStatus

