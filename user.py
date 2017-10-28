#!/usr/bin/env python3

# Main user charactrer class and methods

import random
import Creatures

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

# Attack function generates random attack damage between 1 and 6 and adusts users hp from creatures attack value

	def attack(self,  monster = None):
		self.hp -= monster.attack
		strike = random.randrange(1,6)
		return strike

# Functions to set self variables

	def setHP(self, new_hp = None):
		self.hp = new_hp

	def setescapeStatus(self, escapeStatus = False):
		self.escapeStatus = escapeStatus

