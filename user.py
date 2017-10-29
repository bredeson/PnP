#!/usr/bin/env python3

#================================================
# Define main user charactrer class and methods
#================================================

import random, time
import creatures
import combatResponses

class Prisoner(object):
	
	def __init__(self, name = 'Unknown', hp = 20, escapeStatus = False, difficulty = 'medium', attack = 6):
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
		self.attack = attack

# Combat function for creature encounters --- calls combatResponses for sassy comments during battle

	def combat(self,  monster = None):
		while monster.hp > 0:
			if self.hp <= 0:
				print('You have died to a',monster.name)
				break
			elif monster.hp > 0:
				new_user_attack = random.randint(1,self.attack)
				new_mon_attack = random.randint(1,monster.attack)
				print(combatResponses.combatResponse_player(self.attack, new_user_attack),'You deal',new_user_attack,'damage','to',monster.name)
				time.sleep(3)
				monster.hp -= new_user_attack
				if monster.hp > 0:
					print('The',monster.name, 'has', monster.hp, 'health remaining')
					time.sleep(3)
					self.hp -= new_mon_attack
					print(combatResponses.combatResponse_monster(monster.attack, new_mon_attack), monster.name, 'does', new_mon_attack, 'damage. Your health is now', self.hp)
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

	def setAttack(self, attack_inc = 0):
		self.attack += attack_inc
		print('Your attack damage has increased to ',self.attack,'.\n', sep = '')
