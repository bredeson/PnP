#!/usr/bin/env python3

# Main user charactrer class and methods

import random
import creatures

class Prisoner(object)
	
	def __init__(self, name = 'Unknown', hp = 20, escapeStatus = False, difficulty = 'medium'):
		self.name = name
		self.hp = hp
		self.escapeStatus = escapeStatus
		self.difficulty = difficulty

# Attack function generates random attack damage between 1 and 6 and adusts users hp from creatures attack value

	def attack():
		self.hp -= creature.Creature.attack
		strike = random.randrange(1,6)
		return strike
